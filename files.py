#file object = open(file_name [, access_mode][, buffering])
#File_name === file Name
#access_mode ===  read, write, append

#r = read only. The file pointer is placed at the beginning of the file.
#rb = read only in binary formate. The file pointer is placed at the beginning of the file.
#r+ read and write. The file pointer is placed at the beginning of the file.
#rb+ read and write in binary formate. The file pointer is placed at the beginning of the file.
# W write only Overwrites the file if the file exists. If the file does not exist, creates a new file for writing
#wb Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
#W+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
#wb+ Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
#a Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
#ab Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.  
#a+ Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
#ab+ Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.


#file.closed Returns true if file is closed, false otherwise.
#file.mode Returns access mode with which file was opened.
#file.mode Returns access mode with which file was opened.
#file.softspace Returns false if space explicitly required with print, true otherwise.

# Open a file
# fo = open("foo.txt", "wb")
# print(fo.name)
# print(fo.closed)
# print(fo.mode)
# # Close opend file
# fo.close()
# print(fo.closed)
# Output :foo.txt
# False
# wb
#True

# Open a file
# fo = open("foo.txt", "w")
# fo.write("Python is a great language.\nYeah its great!!\n")

# # Close opend file
# fo.close()

#fileObject.read([count])
#Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of file.

# Open a file
# fo = open("foo.txt", "r+")
# str = fo.read(10);
# print(str)
# # Close opend file
# fo.close()

#The tell() method tells you the current position within the file

# fo = open("foo.txt","r+")
# str = fo.read(10)
# print(str)
# position = fo.tell()
# print(position)
#The seek(offset[, from]) method changes the current file position
#The offset argument indicates the number of bytes to be moved. 
# The from argument specifies the reference position from where the bytes are to be moved.
# 0 ------------ begining of the file 
# 1 ----- current location
# 2 ---- end of file
# change_position = fo.seek(2,0)
# position = fo.tell()
# print(position)
# fo.close()
# Output: Python is 
# 10
# 2

#Renaming and Deleting Files
#Python os module provides methods that help you perform file-processing operations, 
#such as renaming and deleting files.
# import os
# # os.rename("foo.txt","fooo.txt") # file name changed
# os.remove("fooo.txt")

#The chdir() Method
#You can use the chdir() method to change the current directory.

#The getcwd() method displays the current working directory.

#The rmdir() method deletes the directory, which is passed as an argument in the method.
#Before removing a directory, all the contents in it should be removed.

