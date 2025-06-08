# Dictinory is a collation of keys and pairs
# example
a={"key": "value" ,
    "sameer" : "coder",
    "marks" : 98 , 
    "list" : [9,4,5]
 }
print (a["marks"])
#  properties of python dictionry 
# 1. it is unorderd
# 2.it is mutable
# 3. it is indexed 
# 4. cannot cantain duplicates key 


#  Dictionory method
my_dict = {'name': 'Sameer', 'age': 20}
print(my_dict.get('name'))         # Output: Sameer
print(my_dict.get('gender', 'N/A'))  # Output: N/A
# ✅ 2. dict.keys()
# Returns a view object with all the keys.


print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
# ✅ 3. dict.values()
# Returns a view object with all the values.


print(my_dict.values())  # Output: dict_values(['Sameer', 20])
# ✅ 4. dict.items()
# Returns a view object of key-value pairs.


print(my_dict.items())  # Output: dict_items([('name', 'Sameer'), ('age', 20)])
# ✅ 5. dict.update(other_dict)
# Updates the dictionary with key-value pairs from another dictionary.


my_dict.update({'gender': 'Male'})
print(my_dict)  # Output: {'name': 'Sameer', 'age': 20, 'gender': 'Male'}
# ✅ 6. dict.pop(key, default)
# Removes the key and returns its value.


age = my_dict.pop('age')
print(age)       # Output: 20
print(my_dict)   # Output: {'name': 'Sameer', 'gender': 'Male'}
# ✅ 7. dict.clear()
# Removes all items from the dictionary.


my_dict.clear()
print(my_dict)  # Output: {}
# ✅ 8. dict.copy()
# Returns a shallow copy of the dictionary.


new_dict = my_dict.copy()
# ✅ 9. dict.setdefault(key, default)
# Returns the value of a key; if key doesn't exist, insert it with the default value.


d = {'a': 1}
d.setdefault('b', 2)
print(d)  # Output: {'a': 1, 'b': 2}