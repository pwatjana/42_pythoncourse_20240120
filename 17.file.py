# Present Work directory = PWD
# Change directory = CD ..
'''
import os >> use for file access

cd <path> move to path
cd <dir name> : move to dir name

'''
#get total file size
import os
#import rich # call>>  rich.print
from rich import print # call>> print()

# print (parameters1, 2, 3...)
print("cwd:" ,os.getcwd())
print(os.listdir())

files = os.listdir()
size_in_bytes = 0
for file in files:
    size = os.path.getsize(file)
    size_in_bytes +=size
    print(size, file)
print("size_in_bytes :" , size_in_bytes)

