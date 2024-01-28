# Present Work directory = PWD
# Change directory = CD ..
# print (parameters1, 2, 3...)
# 
# use import os >> for file access
# 1.Open terminal
# 2. navigate terminal to work folder or (dir)
#     How to navigate in terminal
#     PWD = check current path  
#     ls  - list all files and folders inside a directory
#     mkdir = create new folder >> mkdir folder name
#     CD [folder name] = change directory 
#     CD .. to change the current working directory in various operating systems
#     >notice change of work path end with select directory
#         #1)PS C:\Users\66869\OneDrive\Documents\GitHub\42_pythoncourse_20240120\42_pythoncourse_20240120> ls
#         #1)output[text]
#         #2)PS C:\Users\66869\OneDrive\Documents\GitHub\42_pythoncourse_20240120\42_pythoncourse_20240120> cd text
#         #3)PS C:\Users\66869\OneDrive\Documents\GitHub\42_pythoncourse_20240120\42_pythoncourse_20240120\text>
# ''''''3.Create a new python script with .py extension
# os.chdir(path) = change the working directory
# os.getcwd() = get current working directory
# os.listdir([path]) = list all files and folders inside a given path,
# if no argument is provided it will return a list of objects inside the CWD
# os.getsize() = get size of an object/file
#get total file size
import os
#import rich # call>>  rich.print
from rich import print # call>> print()

#print out current work directory
print("cwd:" ,os.getcwd())
#print  out all items in cwd
print(os.listdir())

# change dir to text
# files = list all  files & directories
files = os.listdir()
# size  = sum up all sizes start with 0 bytes
size_in_bytes = 0
# iterate over each item in files
for file in files:
    size = os.path.getsize(file)
    size_in_bytes +=size
    print(size, file)
print("size_in_bytes :" , size_in_bytes)

'''
1 char ~ 1 byte
8 bit = 1 byte
1M char = 1mb
'''

"""
OUTPUT
['0.txt', '1.txt', '2.txt', 'note.txt']
6 0.txt
5 1.txt
7 2.txt
5 note.txt
size_in_bytes : 23
"""