import os
from datetime import datetime
#print(os.path.exists("filename.txt"))

#create if not exist
if os.path.exists("note1.txt"):
    print("note1.txt")
    now = datetime
    print(datetime.now()) #2024-01-27 10:18:18.511823
    with open("note1.txt", "a") as file:
        file.write(f"\n(now)")
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

# OUTPUT 
#c:/Users/66869/OneDrive/Documents/GitHub/42_pythoncourse_20240120/42_pythoncourse_20240120/18.file_write_open_close.py
# note1.txt not exist
# hello
# PS C:\Users\66869\OneDrive\Documents\GitHub\42_pythoncourse_20240120\42_pythoncourse_20240120> 