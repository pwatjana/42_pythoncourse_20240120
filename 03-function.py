# built in function
#print()
#type()
# joint function
#print(type())

# create own function

"""
def function_name(arg1):
    ...
   return..
"""

#strat with 'def' = define follow by function name and () and :
# 1 indent (4 spacebar)
# end with return ...

def add(num:int):# take input value as integer.
    ret = num+1# add 1 to input value
    return ret

'''add(5)'''# call function 
#output = 6


# multiple variables
def sum_num(var1: int, var2: int) ->int:
    ret = var1 + var2
    return ret

'''sum_num(1,4.5)'''
#output = 5.5

# funtion with no input
def hello() ->None:
    print("helloWorld")
hello()
#output 'helloWorld'

'''
print(add(5))
print(sum_num(1,2))
print(hello)
'''

def add_then_sum_itself_then_hello(num: int) ->int:
    ret = add(1) 
    '''take value and process to def add'''
    ret = sum_num(ret,num) 
    '''get ret value from def add then go to def sum_num'''
    hello()
    return ret
'''print("add_then_sum_itself_then_hello(5):")'''

my_result = add_then_sum_itself_then_hello(5)
print(my_result)

'''
refer 5 as num value to def add_then_sum_itself_then_hello.

ret = add (1) 
    output =2 because add(1) mean use num=1 + 1 in def add.

ret = sum_num(ret,num)
    then process ret again with sum_num(ret=2,5) in def sum_num(2,5)
    output = 7
return ret = 7
then print hello() and retun ret

output
helloWorld
helloWorld
7
'''
