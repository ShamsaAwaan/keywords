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
for i in range (1,11):
    print(i)

for num in range (3,8):
    if num == 5:
        continue
    else: 
        print(num)


months = ['january',['june'],['april']]
for month in months:
    pass
print(months)

sum= 0
for i in range(2, 22, 2):
    print(i)
    sum = sum + i
print(sum)
numbers= [1,2,3,4,5]
for i in numbers:
    square = i ** 2
    print("Square of:", i, "is:", square)


numbers = [10,20,30]
sum = 0
for i in numbers:
    sum= sum + i
print(sum)
list_size = len(numbers)
print(len(numbers))
average = sum/ list_size
print(average)


for i in range(1,11):
    if i % 2 == 0:
        print('Even Number:', i)
    else:
        print('odd:', i)




numbers = [ 1,2,4,6,7,8,9,155,156]
for i in numbers:
    if i > 15:
        break
    else:
        print(i)


name= 'shamsa'
count= 0
for char in name:
    if char == 's':
      count= count +1
print('total num of s is:', count)


for i in range(1, 6):
    print(i)
else:
    print("Done")

list1= [10,20,30,40,15]
for num in reversed(list1):
    print(num)

print("Reverse numbers using for loop")
num= 5
for num in (range(num, -1, -1)):
    print(num)

numbers= [1,2,3,4]
for i in numbers[::-1]:
    print(i)


rows = 5
for i in range(1, rows +1):
    for j in range(1,i+1):
        print("*", end="")
    print('')
        
for i in range(1, 6):
    print('multiplication table of :', i)
    count =1
    while count < 11:
          print(i* count, end=' ')
          count= count+1
    print('\n')

odd = [1,5,7,9]
even= [i+1 for i in odd if i % 2 ==1]
print(even)
for i in odd:
    if i%2==1:
       i=i+1
       print(i)

numbers = [4,2,4,7,8]
for i, v in enumerate(numbers):
    print('Numbers[', i, '] = ', v)

    
numbers = [1,2,4,6,8]
size = len(numbers)
for i in range(size):
    print('Index:', i," ", 'Value:', numbers[i])

name= "Charlie"
for i in name:
    print(i, end= ' ')
print('\n')


name= "Charlie"
for i in name[::-1]:
    print(i, end= ' ')
print('\n')


name = "Charlie is master"
for i in name[2:7:2]:
    print(i, end= ' ')
print('\n')
for word in name.split():
    print(word)

numbers = [2,3,5,6,7]
for num in numbers:
    print(num)
print('\n')
numbers = [1,2,3,4,5]
print(len(numbers))
size= len(numbers)
for i in range(size):
    print(numbers[i])
print('\n')
numbers = [1,2,3,7,8]
[print(i) for i in numbers]

dict1= {1:"Apple", 2:"Ball"}
dict2= {"Apple":"BMW", "Ball":"BLACK"}
print('\n')
for key in dict1:
    print(key)
print('\n')
for value in dict1.values():
    print(value)