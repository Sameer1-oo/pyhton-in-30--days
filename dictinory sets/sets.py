# set is the collation of non -repetitive elements define obejct
# set={4,5,6,5}
# set = set() it is way toi write a emopty set  not set = {}
my_set = {1, 2, 3}
another_set = set([4, 5, 6])


# propetes of sets 
# # 1. set are unordered  => elements order does not matter 
# 2. setr are unindexed  => cannot way to change items insets 
# 3. there is no way o changew thge set element value 
# 4. set cannmot the duplicate valkues method of sets 
 

#   Method of sets 

# Basic Set Methods
# 1. add()
# Adds an element to the set.


my_set = {1, 2}
my_set.add(3)
print(my_set)  # Output: {1, 2, 3}
# 2. remove()
# Removes a specific element. Gives an error if the element is not found.


my_set.remove(2)
# 3. discard()
# Removes a specific element. No error if not found.


my_set.discard(5)  # No error
# 4. pop()
# Removes and returns a random element.


element = my_set.pop()
print(element)
# 5. clear()
# Removes all elements from the set.


my_set.clear()
# 🔹 Set Operations
# # 6. union() / |
# Returns a new set with elements from both sets.


a = {1, 2}
b = {2, 3}
print(a.union(b))  # Output: {1, 2, 3}
# 7. intersection() / &
# Returns common elements.


print(a & b)  # Output: {2}
# 8. difference() / -
# Returns elements in the first set but not in the second.


print(a - b)  # Output: {1}
# 9. symmetric_difference() / ^
# Elements in either set but not both.


print(a ^ b)  # Output: {1, 3}
# 10. issubset() / issuperset()
# Check if one set is a subset or superset of another.


a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))     # True
print(b.issuperset(a))   # True
# 🔹 Example Use Case

students = {"Sam", "Ravi", "Priya", "Sam"}
print(students)  # Output: {'Sam', 'Ravi', 'Priya'} → no duplicates