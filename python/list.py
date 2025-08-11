list1 = [10, 20, 30, 40]
print("List1:", list1)

mixed_list = [1, "apple", 3.14, True]
print("Mixed List:", mixed_list)

# From tuple
list_from_tuple = list((5, 6, 7))
print("List from tuple:", list_from_tuple)

# Empty list
empty_list = []
print("Empty List:", empty_list)


print("First element:", list1[0])
print("Last element:", list1[-1])
print("Slicing [1:3]:", list1[1:3])

if 20 in list1:
    print("20 is in list1")


list1.append(50)   # Add at end
print("After append:", list1)

list1.insert(2, 25)  # Add at index 2
print("After insert:", list1)

list1.extend([60, 70])  # Add multiple from another iterable
print("After extend:", list1)


list1.remove(25)  # Remove first occurrence
print("After remove:", list1)

popped = list1.pop()  # Remove last item
print("Popped item:", popped)
print("After pop:", list1)

popped_at_index = list1.pop(1)  # Remove at index
print("Popped at index 1:", popped_at_index)
print("After pop index:", list1)


list1[0] = 100
print("After changing first element:", list1)

list1[1:3] = [200, 300]  # Replace slice
print("After slice assignment:", list1)


for item in list1:
    print("Item:", item)


squares = [x*x for x in range(1, 6)]
print("Squares:", squares)

#Sorting 
numbers = [5, 2, 9, 1]
numbers.sort()
print("Sorted Asc:", numbers)

numbers.sort(reverse=True)
print("Sorted Desc:", numbers)

# Sort without modifying original
sorted_numbers = sorted(numbers)
print("Sorted copy:", sorted_numbers)


print("Length:", len(numbers))
print("Count of 2:", numbers.count(2))
print("Index of 9:", numbers.index(9) if 9 in numbers else "Not found")

numbers.reverse()
print("Reversed:", numbers)

# Copy
numbers_copy = numbers.copy()
print("Copy of numbers:", numbers_copy)

# Clear list
numbers_copy.clear()
print("Cleared list:", numbers_copy)

# Built-in Functions 
nums = [10, 20, 30]
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Any True:", any(nums))
print("All True:", all(nums))
