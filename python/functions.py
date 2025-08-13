def add (num1=2 ,num2=3):
   a=num1+num2
   print(a)
add()

def message():
    print("hello bravo")
message()

def course(name="bravo", course_name="english"):
    print(name, course_name)
course()

def course(name="bravo", course_name="english"):
    a=(name, course_name)
    return a
res= course()
print(res)

def even_odd(a):
    if a % 2 == 0:
        print('number even')
    else:
        print('odd  num')
even_odd(12)

def factorial(x):
    '''this is x factorial'''
    return x
print(factorial.__doc__)

def courses(name1="brao", course_name1="english",
    name2="brvo", course_name2="englih",
    name3="brav", course_name3="englis",
    name4="brao", course_name4="engli"):
    a=(name1, course_name1)
    b=(name2, course_name2)
    c=(name3, course_name3)
    d=(name4, course_name4)
    return a,b,c,d
a,b,c,d = courses()
print(a)
print(b)
print(c)
print(d)
print('\n')
x=5
def function1():
    print("value in first fun:", x)
def function2():
    x=55
    print("value in second fun:", x)

def function3():
    print("value in second fun:", x)

function1()
function2()
function3()