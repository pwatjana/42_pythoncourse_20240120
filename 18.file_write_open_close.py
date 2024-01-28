import os
from datetime import datetime
#print(os.path.exists("filename.txt"))
print(os.path.exists("0.txt"))
print(os.path.exists("3.txt"))
# '''output check from dir : Github\42_pythoncourse_20240120\42_pythoncourse_20240120\text>
# >>> print(os.path.exists("0.txt"))
# True
# >>> print(os.path.exists("3.txt"))
# False
# '''

#create if not exist
if os.path.exists("note1.txt"):
    print("note1.txt")
    now = datetime.now() 
    print(datetime())# without .now() will get result as  <class 'datetime.datetime'>
    print(datetime.now()) #current date and time in std format :2024-01-27 10:18:18.511823
    with open("note1.txt", "a") as file:
        file.write(f"\n {now}")
else : 
    print("note1.txt not exist")

    ''' write file 1 ,  if use .write() must have .close() 
    file = open("note.txt","w")
    file.write("This is a note\n")
    file.close()
    '''
    # write file2 
    with open("note1.txt","w") as file:
        file.write("hello")


# open read mode
with open("note1.txt", "r") as file:
    print(file.read())

# OUTPUT > write
#c:/Users/66869/OneDrive/Documents/GitHub/42_pythoncourse_20240120/42_pythoncourse_20240120/18.file_write_open_close.py
# note1.txt not exist
# hello
# note1.txt exist  
#  <class 'datetime.datetime'>
#  <class 'datetime.datetime'>
#  2024-01-28 08:35:36.250432
#  2024-01-28 08:35:40.966722