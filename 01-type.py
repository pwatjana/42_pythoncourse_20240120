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

type(a>b or a>c)
#<class 'bool'>