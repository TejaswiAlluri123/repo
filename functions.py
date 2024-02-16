# Function Arguments
# You can call a function by using the following types of formal arguments −

# Required arguments :Required arguments are the arguments passed to a function in correct positional order. 
#Here, the number of arguments in the function call should match exactly with the function definition.
# Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print (str)
#    return str

# # Now you can call printme function
# result = printme("teja")
# print(result)
# Output: teja
# teja


# Keyword arguments:
# Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print (str)
#    return

# # Now you can call printme function
# printme( str = "My string")

# Output : My string
# Function definition is here
# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# # Now you can call printinfo function
# printinfo( age = 50, name = "miki" )
# output:Name:  miki
# Age  50

# Default arguments
# Function definition is here
# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# # Now you can call printinfo function
# printinfo( age = 50, name = "miki" )
# printinfo( name = "miki" )

# output:Name:  miki
# Age  50
# Name:  miki
# Age  35

# Variable-length arguments

# def printinfo( arg1, *vartuple ):
#    "This prints a variable passed arguments"
#    print ("Output is: ")
#    print (arg1)
   
#    for var in vartuple:
#       print (var)
#    return

# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50 )
# Output is: 
# 10
# Output is: 
# 70
# 60
# 50

# The Anonymous Functions
# These functions are called anonymous because they are not declared in the standard manner by using the 
# def keyword. You can use the lambda keyword to create small anonymous functions.
# Lambda forms can take any number of arguments but return just one value in the form of an expression. 
# They cannot contain commands or multiple expressions.
# An anonymous function cannot be a direct call to print because lambda requires an expression.
# Lambda functions have their own local namespace and cannot access variables other than those in their 
# parameter list and those in the global namespace.
# Although it appears that lambdas are a one-line version of a function, they are not equivalent to 
# inline statements in C or C++, whose purpose is to stack allocation by passing function, during invocation 
# for performance reasons.

# sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
# print ("Value of total : ", sum( 10, 20 ))
# print ("Value of total : ", sum( 10, 20 ))
# print ("Value of total : ", sum( 10, 20 ))
# #Output:
# Value of total :  30
# Value of total :  30
# Value of total :  30

#  There are two basic scopes of variables in Python −

# Global variables
# Local variables
# Variables that are defined inside a function 
# body have a local scope, and those defined outside have a global scope.



def myfunction():
    a = 4
    b = 5
    c= a+b
    return c
    print(C)

#result = myfunction()
