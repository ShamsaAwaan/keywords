import keyword
# keyword having a keyword list inside kwlist
print(keyword.kwlist)
print(keyword.iskeyword('if'))
print(keyword.iskeyword('range'))
x=2
y=3
z=2
print(x is y)
print (x is z)
list=[1.2,3,4]
number=4
if number in list:
    print("number is present")
else:
    print("number is not present")
# if,elif,else keywords
x= 75
if x > 100:
        print('x is greater than 100')
elif x > 50:
        print('x is greater than 50 but less than 100')
else:
        print('x is less than 50')
  # for and while (conditional keywords)
print('for loop to display first 5 numbers')
for i in range(5):
    print(i,end='')

print('while loop to display first 5 numbers')
n = 0
while n < 5:
    print(n, end=' ')
    n = n + 1 
    # class ,object,instance
class Student:
    def __init__ (self,name, age):
       self.name = name
       self.age = age
    def show(self):
        print (self.name,self.age)
       
s= Student ('Shamsa', 22)
s.show()
#with keyword
with open ('simple.txt','r', encoding='utf-8') as fp:
    print(fp.read())
