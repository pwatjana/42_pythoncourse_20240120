'''
string is text in ''' ''' or """ """

if have to add ' in text:
"This is bob's cat"
'This is bob\'s cat'
" \"This is bob's cat"\ "

\t = add tab between text
\\
\n = new line
'''
print("This is bob\tcat")
'''output: This is bob     cat'''
print("This is bob\\'s cat")
'''output: This is bob\'s cat'''
print("This is bob's cat")

print('\"This is bob\'s cat"')
'''"This is bob's cat"'''

#string is list like object.
my_string ='abcfghijk'
print(my_string[1:3])
'''bc'''
print(my_string[1:-3])
'''bcfgh'''

for i in my_string:
    print([1])

#check word contain in text
"ab" in my_string
'''outputTrue'''

#concatenate string
my_string1= "Hello" + " " + "World"
print(my_string1)

#string method, a function attached with object  
#my_string. >> then will see a list of method to select
my_string.upper()
print(my_string)
''''output "ABCFGHIJK'''

#isalnum ' check if text are all num
sen1 = "hello1"
sen1.isalnum()
sen1.isalpha()
'''output true >> check and return only true or false'''

#split ' split string to array that have string
sen2 = "my name is, punch"
sen2.split() 
'''output ['my', 'name', 'is', 'punch']'''
sen2.split(',')
'''output ['my name is', ' punch']'''

#join lists
list3 = ['a','b','c']
"-".join(list3)
'''output 'a-b-c' '''