import os
from datetime import datetime
#print(os.path.exists("3.txt"))

#create if not exist
if os.path.exists("note.txt"):
    print("note.txt")
    now = datetime
    print(datetime.now()) #2024-01-27 10:18:18.511823
    with open("note.txt", "a") as file:
        file.write(f"\n(now)")
else : 
    print("note.txt not exist")

    ''' write file 1 ,  if use .write() must have .close() 
    file = open("note.txt","w")
    file.write("This is a note\n")
    file.close()
    '''
    # write file2 
    with open("note.txt","w") as file:
        file.write("hello")


# open read mode
with open("note.txt", "r") as file:
    print(file.read())
