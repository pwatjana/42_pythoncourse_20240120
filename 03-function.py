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
    ret = sum_num(ret,num)
    hello()
    return ret
print("add_then_sum_itself_then_hello(5):")

my_result = add_then_sum_itself_then_hello(5)
print(my_result)

'''
output
helloWorld
7
'''