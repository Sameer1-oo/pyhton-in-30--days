# we want list for store any data type elmenets od value in list 
# strings are immutable that cannot changed . but list (array) are mutable it is changable . we  can assigen the value 
# example
list=["apple","orange","rohan ",9,0.236]
print(list[0])
list[0] =" graopes"
print(list[0])
# list has indexing satrt from 0
# many list method in python the help arragene and edit the list in several ways pythonCopyEdit


#  1. append()
# Adds an element to the end of the list.


fruits = ['apple', 'banana']
fruits.append('mango')
print(fruits)  # ['apple', 'banana', 'mango']
# ✅ 2. extend()
# Adds multiple elements to the end.


fruits = ['apple']
fruits.extend(['banana', 'mango'])
print(fruits)  # ['apple', 'banana', 'mango']
# ✅ 3. insert()
# Inserts an item at a given index.


fruits = ['apple', 'mango']
fruits.insert(1, 'banana')
print(fruits)  # ['apple', 'banana', 'mango']
# ✅ 4. remove()
# Removes the first matching element.


fruits = ['apple', 'banana', 'apple']
fruits.remove('apple')
print(fruits)  # ['banana', 'apple']
# ✅ 5. pop()
# Removes and returns an item at a given index (default is last).


fruits = ['apple', 'banana', 'mango']
fruits.pop()
print(fruits)  # ['apple', 'banana']
# ✅ 6. index()
# Returns the index of the first match.


fruits = ['apple', 'banana', 'mango']
print(fruits.index('banana'))  # 1
# ✅ 7. count()
# Returns how many times an element appears.


numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))  # 3
# ✅ 8. sort()
# Sorts the list in ascending order.


nums = [3, 1, 4, 2]
nums.sort()
print(nums)  # [1, 2, 3, 4]
# ✅ 9. reverse()
# Reverses the list in-place.


nums = [1, 2, 3]
nums.reverse()
print(nums)  # [3, 2, 1]
# ✅ 10. copy()
# 
# Returns a shallow copy of the list.


fruits = ['apple', 'banana']
new_list = fruits.copy()
print(new_list)  # ['apple', 'banana']
# ✅ 11. clear()
# Removes all items from the list.


fruits = ['apple', 'banana']
fruits.clear()
print(fruits)  # []