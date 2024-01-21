"""#flow control

#ticket price based on age

ADULT_AGE = 18
SENIOR_AGE = 65
age = input("How old are you: ")
age = int(age)

'''
if condition1 :
    # if condition 1 do this
elif condition2:
    # if condition 2 do this
else :
    # if non do this. optional
"""

ADULT_AGE = 18
SENIOR_AGE = 65
age = input("How old are you: ")
age = int(age)

if age < 0:
    print("invalid age")
    exit()

if age >= SENIOR_AGE:
    print("Baht 200")
elif age >= ADULT_AGE:
    print("Baht 256")
elif age < ADULT_AGE:
    print("Baht 150")
    

