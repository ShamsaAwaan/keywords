
# Using {}
sample_set = {"Mark", "Jessa", 25, 75.25}
print("Sample Set:", sample_set)

# Using set() constructor
book_set = set(("Harry Potter", "Atlas Shrugged", "Angels and Demons"))
print("Book Set:", book_set)

# From list (duplicates removed)
number_list = [20, 30, 20, 30, 50, 30]
unique_numbers = set(number_list)
print("Unique Numbers:", unique_numbers)

# Empty set
empty_set = set()
print("Empty Set:", empty_set)

for book in book_set:
    print("Book:", book)

if "Harry Potter" in book_set:
    print("'Harry Potter' found!")

# Adding & Removing Items
fruits = {"apple", "banana", "cherry"}
fruits.add("grape")
print("After add:", fruits)

fruits.remove("banana")  # KeyError if missing
print("After remove:", fruits)

fruits.discard("mango")  # Safe if missing
print("After discard:", fruits)

# --- Set Operations ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a-b):", a - b)
print("Symmetric Difference:", a ^ b)

# Update in place
a.update(b)
print("After update:", a)

# Reset for next example
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.intersection_update(b)
print("After intersection_update:", a)

set1 = {1, 2}
set2 = {1, 2, 3}
set3 = {4, 5}

print("set1 is subset of set2:", set1.issubset(set2))
print("set2 is superset of set1:", set2.issuperset(set1))
print("set1 is disjoint from set3:", set1.isdisjoint(set3))

# Copy
set_copy = set1.copy()
print("Copy of set1:", set_copy)

# Sorting sets (convert to list)
sorted_set = sorted(set2)
print("Sorted set2:", sorted_set)

# Built-in functions
nums = {10, 20, 5, 15}
print("Max:", max(nums))
print("Min:", min(nums))
print("Any > 0:", any(nums))
print("All > 0:", all(nums))

# --- Immutable Set ---
fs = frozenset([1, 2, 3])
print("Frozenset:", fs)

# Nested Sets using frozenset
nested = {frozenset([1, 2]), frozenset([3, 4])}
print("Nested Set:", nested)

# --- Set Comprehension ---
squares = {x*x for x in range(1, 6)}
print("Squares:", squares)
