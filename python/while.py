count = 1
while count <3:
    print(count)
    count=count+1
print('\n')
count= 1
while count<5:
    print(count)
    count= count+1
print('\n')
count =0
number= 180
while number > 10:
    number= number/3
    count=count+1
print('total iteration', count)
print('\n')


   
#number = int(input("Enter a number between 100 and 500: "))
#while 100 <= number <= 500:
     #print("Number is correct.")
     #number = int(input("Enter a number between 100 and 500: "))
#else:
     #
     # print("Number is not correct.")

print('\n')
#while True:
    #print('hello')
#print('\n')
#n= int(input('Please enter Number'))
#while n > 0:
 #   if n % 2 == 0:
  #      print(n, 'is a even number')
  #  else:
    #    print(n, 'is odd number')
  #  n = n - 1

name= "Bravo"
print(len(name))
size = len(name)
i = 0
while i < size:
    if name[i].isdecimal():
        break;
    print(name[i], end=' ')
    i = i+1
print('\n')  
name= 'Shamsa'
size= len(name)
i= -1
while i < size -1:
    i= i +1
    if not name[i].isalpha():
        continue
    print(name[i], end=" ")
print('\n') 
n= 4
while n >0:
    n=n -1
    pass
print('\n') 
i =0
while i <=5:
    j= 0
    while j<i:
        print("*", end= " ")
        j=j+1
    print (' ')
    i=i+1
print('\n') 
i=0
while i < 5:
    for j in range(0, i+1):
        print("*", end=" ")
    print('')
    i=i+1
print('\n') 
i= 0
while i<=5:
    print(i)
    i= i +1
else:
    print("done, succesfully while loop executed")
#i= 0
#while i<=5:
   # print(i)
#   if i ==3:
#    break
  #  i= i +1
#else:
  #  print("done, succesfully while loop executed")
print('\n')

i= 10
while i >=0:
    print(i,end=' ')
    i= i-1 
print('\n')
name= "Shamsa"
i = 0
bravo = len(name) -1
while i <= bravo:
    print(name[i])
    i= i+1
print('\n')
num=[1,2,3,4,5,6,7]
name=["ALPHA", "BRAVO", "CHARLIE"]
size=len(name)
i= 0
while i <size:
    print(name[i])
    i=i+1
print('\n')
#num=[1,2,3,4,145,120]
#for i in num:
  #  if i >100:
 #       break
#    print('current number', i)
print('\n')

numbers=[2,3,4,5,7,88,999]
for i in numbers:
    print('current number is',i)
    if i >10:
        continue
    square=i*i
    print('square of number', square)
print('\n')
name='Sh a ms a'
print(len(name))
size=len(name)
i=- 1
while i < size -1: 
    i= i+1
    if name[i].isspace():
        continue 
    print(name[i],end= " ")  
print('\n')
###############
for i in range(1,11):
    print('multiplication table of', i)
    for j in range(1,11):
        if j == 5:
           continue
        print(i*j, end=" ")
    print('')
###############
print('\n')
for i in range(1,11):
    if i%2==0:
        continue
    print('multiplicTion table of', i)
    for j in range(1,11):
        print(i*j,end= ' ')
    print('')

print('\n')
#for i*j in range (1,11):
 #   for j in range(1,11):
  #      print(i*j, end=' ')
   # print()
print('\n')
n =5
for i in range(1, n+1):
    for j in range(1,i+1):
        print("+",end=" ")
    print('')

i=1

print('\n')
for i in range(5):  # Outer loop for rows
    for j in range(3):  # Inner loop for columns
        print('*', end=' ')
    print()  # Move to the next line after each row
print('\n')
for i in range(4):
    for j in range(4):
        if j==i:
            break
    print(i,j)
print('\n')
first=[2,4,6]
second=[2,4,6]
for i in first:
    for j in second:
        if i == j:
            continue
        print(i, '*', j, '= ', i * j)
print('\n')
first = [2, 3, 4]
second = [20, 30, 40]
final = []
for i in first:
    for j in second:
        final.append(i+j)
print(final)
i=1
while i<= 5:
    j=1
    while j<=10:
        print(j, end=(''))
        j=j+1
    i=i+1
    print()
print('\n')
#first_number=int(input('enter your first number:'))
#second_number=int(input('enter your second number:'))
#rint(first_number)
#print(second_number)
#sum= first_number + second_number
#print(sum)

#marks= float(input('Enter marks'))
#print("\n")
#print('student marks',marks)
#print('type is:', type(marks))

#print('\n')
#number=int(input('enter ur number:'))
#second_number=float(input('enter ur number:'))
#print(number)
#print(second_number)
#product = number * second_number
#print('multipication is',product2)
name,age,rollno= input('enter ur name, age, rollno').split()
print('student details:', name, age, rollno)