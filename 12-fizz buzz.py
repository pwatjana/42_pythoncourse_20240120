count = 0
while count < 20:
    #print (count)
    count = count +1
    if count % 3 == 0 and count % 5 == 0:
        print("fizz", " buzz")
    elif count % 5 == 0:
        print("buzz")
    elif count % 3 == 0:
        print("fizz")
    else:
        print(count)


"""
target:
- loop number 1-20
- if input % 3 =0 print fizz
- if input % 5 =0 print buzz
- if input can %3 and %5 =0 print fizz buzz (__ and___)
- if input %3 and %5 != 0 print num
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizz  buzz
16
17
fizz
19
buzz
"""

"""
xzeed 's code
for i in range(1,21):
# use range will not count 21 process will stop at last num -1
# range(1,21) > output 1-20
# range(1,20+1) > output 1-20

    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
"""


"""
#use lists 
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for num in nums:
    print(num)
    if num%3==0 and num%5==0:
        print("fizz buzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(nums)
"""



