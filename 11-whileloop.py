''' while condition : 'check true false
        do....
'''
"""
from time import sleep
while True:
    print("hello")
    sleep(1)
# print text for time in sleep. non stop unless value change
'''ctrl + c = esc run terminal'''
while False:
    print("hello")
    sleep(1)
    
"""

count =0
while count < 5:
    print (count)
    count = count +1

count =5
while count > 0:
    print (count)
    count = count -1

# break to exit loop
count =0
while count < 100:
    print (count)
    count = count +1
    if count ==5:
        break
    
#continue
count = 0
while count < 100:
    print (count)
    count = count +1
    if count == 5:
        continue
    if count == 6:
        continue
    print(count)