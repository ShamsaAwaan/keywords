
tuple1 = (10, 20, 30)
print("Tuple1:", tuple1)

mixed_tuple = (1, "apple", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

# From list
tuple_from_list = tuple([4, 5, 6])
print("Tuple from list:", tuple_from_list)

# Empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Single element tuple
single_tuple = (5,)
print("Single Element Tuple:", single_tuple)

# Tuple without parentheses 
tuple_packed = 1, 2, 3
print("Packed Tuple:", tuple_packed)

#Accessing Elements
print("First element:", tuple1[0])
print("Last element:", tuple1[-1])
print("Slicing [1:3]:", tuple1[1:3])

if 20 in tuple1:
    print("20 is in tuple1")

for item in tuple1:
    print("Item:", item)

#Workaround for "Updating" Tuples 
temp_list = list(tuple1)
temp_list[0] = 100
tuple1 = tuple(temp_list)
print("Updated Tuple:", tuple1)

# Concatenation 
t1 = (1, 2)
t2 = (3, 4)
print("Concatenated:", t1 + t2)
print("Repeated:", t1 * 3)

# Unpacking Tuples
a, b, c = (10, 20, 30)
print("Unpacked values:", a, b, c)


#Built-in Functions 
nums = (10, 20, 30)
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Count of 20:", nums.count(20))
print("Index of 30:", nums.index(30))

tuple_comp = tuple(x*x for x in range(1, 6))
print("Squares Tuple:", tuple_comp)
