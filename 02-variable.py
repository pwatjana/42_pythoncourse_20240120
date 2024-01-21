# How to store a value
# set variable 
my_variable = 10+1
print(my_variable)
# program will output 11
my_variable = 5
print(my_variable)
# program will output 5

marble = 8
snoopy = 9
print(marble+snoopy)
# program will output 17

marble = "four"
snoopy = "nine"
print(marble+snoopy)
# program will output fournine

marble = 8
snoopy = "nine"
print(marble+snoopy)
# program will output TypeError: unsupported operand type(s) 
#for +: 'int' and 'str'
print(marble,snoopy)
# program will output: 8 nine

#Variable name rule
#Cannot start with number
#4 = "nine"
# syntax error

#Cannot name same as function
#print = 5 >> Wrong

#Correct name style
My_Var_name = 8 # Snake case
MyVarName = 8# Camel case , but not recommend
MY_VALUE_NUM =3.14 
# All caps, used for constants value that we will not change

