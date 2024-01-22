type(1)
#<class 'int'>
### Int = number value without decimal.###
type(0.1)
#<class 'float'>
### Int = number value with decimal.###

print(type(1+4))
print(type(2.1+4))
#>>> print(type(1+4))#
#<class 'int'>#
#>>> print(type(2.1+4))#
#<class 'float'>#


type("9")
type("nine0")
#<class 'str'>#

a = 1
b = 2
c = 1
type(a>b or a>c)
#<class 'bool'>

import random
hand = random.choices(["rock", "paper", "scissor"])
print(hand)
print(type(hand))
#output 1st time > ['paper']
#output <class 'list'>

import random
hand = random.choices(["rock", "paper", "scissor"])[0]
print(hand)
print(type(hand))
#output 1st time > scissor
#<class 'str'>