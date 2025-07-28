x=20
print(x)
l= 4; b= 10
print('area of rectangle;', l*b)
# NEWLINE use for explicit continuation(we can extend a statement on multiple lines)
addition= 10+20+\
          20+10+\
          20+10+30
print(addition)         
# multiple lines  but single statement called implicit continuation
addition= (10+20+
           20+10+
           20+10+30)
print(addition)
# to make lists we pass strings in single quotes followed by comma and use square braces.
list= ['Shamsa',
      'Shaheen',
       'Ali']
print(list)
# to pass variables with vlaues we use curly braces.
Student= {'Shamsa': 20,
          'Shaheen':10,
          'Ali': 5
         }
print(Student)
# when we want to access fun in future ,dont want to code now then we use PASS statement.
def fun1():
     pass    
# del list when we del variables we cannot access it later
x=2
y=3
# print(x*y)
# del x, y
# print(x*y)
# to return value from called funtion we use RETURN Statement
def addition(num1=10, num2=10):
    return num1 + num2

b = addition()
print(b)

# to import modules and also classes from modulue we usd IMPORT STATEMENT
import datetime
date= datetime.datetime.now()
print(date)

numbers=[10,40,120,230]
for i in numbers:
    if i >100:
        print('current number',i)
        break
