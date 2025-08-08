list1=list((1,2,3))
print(list)
list2=[1,2,3]
print(list2)
list3=["ali",1.0,3]
print(list3)

list4 = [3,5,'a','b']

for item in list4:
    print(item)
print('\n')
list5 = [3,5,'a','b']
len(list5)
for i in range(0, len(list5)):
    print(list5[i])
print('\n')
list6 = [3,5,'a','b']
list6.append('c')
print(list6)
list6.append([2,3,4])
print(list6)
print('\n')
list7 = [3,5,'a','b']
list7.insert(5,7)
print(list7)
print('\n')
list8 =[19,2,3,4,5]
list8[1:4]=[19,2,3,4,5]
print(list8)