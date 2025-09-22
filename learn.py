# variable assignment
'''
x=5
print(x)
'''
#data types
'''
int,float,str,complex,bool
'''
#data type 
''' 
a=int(5)
b=float(5.3)
c="hello"
d=4+3j
print(type(a)
      ,type(b),type(c),type(d))
print(a,b,c,d)
'''
#length of string
'''
a="hello"
print(len(a))
'''
#str slicing

'''
a="hello world"
print(a[3:9])
'''
#str modification
'''
lower()
upper()
strip()
replace()
split()

'''
"""
a=" Hello World "
print(a.lower())
"""
#str concatenation
'''
a="hello"
b="world"
print(a+" "+b)
'''
#str replace
'''
x="hello earth"
print(x.replace("earth","world"))
'''
#str split
'''
x="hello world earth"
print(x.split())
''' 
#str formatting
'''
Name="John"
age=23
txt="my name is{} and i am {}"
print(txt.format(Name,age))
'''
#str formating2
'''
name="dharshini"
age=20
txt=f"im {name},and im {age} old"
print(txt)
'''
#boolean
""" true and false
all string are true except empty string"""
'''
x="hello"
print(bool(x))
'''
#operators
'''
      1. Arithmetic operators
      2. Assignment operators
      3.logical operators
      4.comparison operators
      5.identity operators
      6.membership operators
      7.bitwise operators
      '''
#arithmetic operators
'''
x=4
y=5
print(x+y)
print(x-y)
print(x*y)
print(x/y)  
print(x%y)
print(x**y)'''
#task 1
'''
number=23
"""

the output will be 5
"""
print(number)
'''
#task 1 solution
'''
number=23
print(number//4)
'''

#assignment operators
'''
a=5
a+=3
                         # a=a+3
print(a)

'''

#Comparison operators

'''
a=5
b=5
c=a==b
d=a!=b
e=a>b 
f=a<b
g=a>=b
h=a<=b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
'''
#logical operators
'''
#and
name="dharshini"
age=20
print(name=="dharshini" and age==20) #true
print(name=="dharshini" and age==25)  #false
#or
print(name=="dharshini" or age==25)  #true
print(name=="dharshini1" or age==25) #false
#not
print(not(name=="dharshini" and age==20)) #false
print(not(name=="dharshini" and age==25)) #true
'''
#membership operators
'''
name="dharshini","john","jane"
print("john" in name) #true
print("dharshini" not in name) #false
'''
#bitwise operators
'''
a=5  #binary  0101
b=3  #binary  0011
print(a&b) #binary 0001  output 
'''