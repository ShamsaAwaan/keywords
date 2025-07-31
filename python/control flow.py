a = '23'
print(type(a))
num=int(a)
print(num)
print(type(num))
number = 6
#if number >5:
    #print(number*number)
#print('next code')
#password = input('enter pass')
#if password == "abc":
 #   print("correct password")
#else:
    #print("incorrect")

def user_check(choice):
    if choice == 1:
        print("Sir")
    elif choice == 2:
        print("ma'am")
    elif choice == 3:
        print("student")
    else:
        print("none")
user_check(3)

#num1= int(input('first num'))
#num2= int(input('2nd num'))
#if num1>= num2:
   # if num1== num2:
     #  print(num1, 'and',num2, 'are equal')
   # else:
      #  print (num1, 'is greater', num2)
#else:
  #print(num1, 'is smaller than',num2)
number = 56
if number > 0: 
    print("+")
else:
    print("_")
x= 1
while x <= 5:
    print(x);  x= x+1
   

num = 10
sum = 0
i = 1
while i<= num:
    sum = sum+i
    i= i+1
print("sum of first 10 num is:", sum)
