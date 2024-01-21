a=1
b=2
c=1

a==b
a==c
a!=b
a!=c

a>b
a<b
a<=b
a>=b

a>b and a>c
a>b or a>c


# 
True and True # true
True and False # false
False and False # false
True or True # true
True or False # true
False or True # true
False or False # false

#casting 'convert data type from string to int

g="50"
print(type(g))
'''<class 'str'>'''
g=int(g)
print(type(g))
'''<class 'int'>'''

print(type(5.6))
'''output 5.6 <class 'float'>'''
print(int(5.6),type(int(5.6)))
'''output 5 <class 'int'>'''