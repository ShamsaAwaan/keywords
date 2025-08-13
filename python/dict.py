# --- Creating Dictionaries ---
dict1 = {"name": "John", "age": 25, "city": "New York"}
print("Dict1:", dict1)

# Using dict() constructor
dict2 = dict(name="Alice", age=30, city="London")
print("Dict2:", dict2)

# Empty dictionary
empty_dict = {}
print("Empty Dict:", empty_dict)

# From list of tuples
dict_from_tuples = dict([("name", "Bob"), ("age", 28)])
print("Dict from tuples:", dict_from_tuples)

# --- Accessing Values ---
print("Name:", dict1["name"])   # Direct access
print("City (safe):", dict1.get("city"))  # get() avoids KeyError
print("Country (default):", dict1.get("country", "Not Found"))

# --- Adding / Updating Items ---
dict1["country"] = "USA"   # Add new
dict1["age"] = 26          # Update existing
print("After add/update:", dict1)

# update() method
dict1.update({"email": "john@example.com"})
print("After update() method:", dict1)

# --- Removing Items ---
dict1.pop("age")   # Removes key & returns value
print("After pop:", dict1)

dict1.popitem()    # Removes last inserted key-value
print("After popitem:", dict1)

del dict1["city"]  # Delete by key
print("After del:", dict1)

dict1.clear()      # Remove all items
print("After clear:", dict1)

# --- Looping Through Dictionary ---
person = {"name": "Alice", "age": 30, "city": "London"}

for key in person:
    print("Key:", key)

for value in person.values():
    print("Value:", value)

for key, value in person.items():
    print(f"{key} → {value}")

# --- Dictionary Comprehension ---
squares = {x: x*x for x in range(1, 6)}
print("Squares dict:", squares)

# --- Nested Dictionaries ---
nested_dict = {
    "emp1": {"name": "John", "age": 25},
    "emp2": {"name": "Alice", "age": 30}
}
print("Nested Dict:", nested_dict)
print("Access emp1 name:", nested_dict["emp1"]["name"])

# --- Copying Dictionaries ---
copy_dict = person.copy()
print("Copy:", copy_dict)

# --- Built-in Functions ---
nums_dict = {"a": 10, "b": 20, "c": 5}
print("Length:", len(nums_dict))
print("Max key:", max(nums_dict))   # Based on key order
print("Min key:", min(nums_dict))
print("Sum of values:", sum(nums_dict.values()))

# --- fromkeys() method ---
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print("From keys:", default_dict)
