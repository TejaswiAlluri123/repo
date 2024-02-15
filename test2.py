import boto3
import concurrent.futures
import datetime
import csv
import logging
import os
import pymssql
from botocore.exceptions import ClientError

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#AWS credentials and region
AWS_REGION = os.environ['AWS_REGION']
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
SECRETS_CLIENT = boto3.client('secretsmanager', region_name=AWS_REGION)

#Function to retrieve password from AWS Secrets Manager
def get_secret(secret_name):
    try:
        response = SECRETS_CLIENT.get_secret_value(SecretId=secret_name)
        secret = response['SecretString']
        return secret
    except ClientError as e:
        logger.error(f"Error retrieving secret {secret_name}: {e}")
        return None

#Function to execute SQL script on RDS instance
def execute_sql_on_instance(instance, script, password):
    try:
        conn = pymssql.connect(server=instance['Endpoint']['Address'],
                               user=instance['MasterUsername'],
                               password=password,
                               database='master',
                               timeout=10)
        cursor = conn.cursor()
        cursor.execute(script)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        logger.error(f"Error executing script on RDS instance {instance['DBInstanceIdentifier']}: {e}")
        return None

# Function to execute SQL script on each database of an RDS instance
def execute_sql_on_databases(instance, password):
    try:
        databases = execute_sql_on_instance(instance, SERVER_SCRIPT, password)
        if databases:
            results = []
            for db in databases:
                db_name = db[0]
                db_result = execute_sql_on_instance(instance, f"USE [{db_name}]; {DB_SCRIPT}", password)
                if db_result:
                    for row in db_result:
                        results.append((instance['DBInstanceIdentifier'], db_name, row[0], row[1]))
                # Execute the stored procedure
                execute_sql_on_instance(instance, f"USE [{db_name}]; {PROCEDURE_SCRIPT}", password)
            return results
        else:
            return []
    except Exception as e:
        logger.error(f"Error executing script on databases of RDS instance {instance['DBInstanceIdentifier']}: {e}")
        return []

# Function to discover RDS instances
def discover_rds_instances():
    try:
        client = boto3.client('rds', region_name=AWS_REGION)
        instances = client.describe_db_instances(Filters=[
            {'Name': 'engine', 'Values': ['sqlserver']},
            # Add more filters if needed for tags
        ])
        return instances['DBInstances']
    except Exception as e:
        logger.error(f"Error discovering RDS instances: {e}")
        return []

# Function to write results to CSV file
def write_to_csv(results):
    filename = f"/tmp/rds_instance_data_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['RDS Instance', 'Database', 'Key', 'Value'])
        csvwriter.writerows(results)
    return filename

# Function to upload file to S3
def upload_to_s3(filename, bucket_name, key):
    s3 = boto3.client('s3', region_name=AWS_REGION)
    try:
        s3.upload_file(filename, bucket_name, key)
        logger.info(f"Uploaded {filename} to S3 bucket {bucket_name} with key {key}")
        return True
    except ClientError as e:
        logger.error(f"Error uploading {filename} to S3 bucket {bucket_name}: {e}")
        return False

# Main Lambda function
def lambda_handler(event, context):
    # Construct the secret name dynamically
    secret_identifier = os.environ.get('SECRET_IDENTIFIER')
    if not secret_identifier:
        logger.error("SECRET_IDENTIFIER environment variable not set")
        return "SECRET_IDENTIFIER environment variable not set"

    secret_name = f"{secret_identifier}-your-unique-identifier"
    
    password = get_secret(secret_name)
    if password is None:
        return f"Error retrieving password from Secrets Manager for secret {secret_name}"
    
    instances = discover_rds_instances()
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(execute_sql_on_databases, instance, password) for instance in instances]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                results.extend(result)
    
    csv_file = write_to_csv(results)
    
    # Upload CSV file to S3
    key = os.path.basename(csv_file)
    if not upload_to_s3(csv_file, S3_BUCKET_NAME, key):
        return f"Error uploading {csv_file} to S3 bucket {S3_BUCKET_NAME}"
    
    return f"Successfully uploaded {csv_file} to S3 bucket {S3_BUCKET_NAME} with key {key}"