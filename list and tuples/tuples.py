# A tuples is an immmutable data type in python we can store diifrnt type of data type in the elemt for m is called tuple 
# they are like string it cannot be changed
# # ⚠️ Note: Tuples are immutable, so they have very few methods compared to lists.

# ✅ 1. count()
# Returns the number of times a value appears in the tuple.

 
t = (1, 2, 2, 3, 2)
print(t.count(2))  # Output: 3
# ✅ 2. index()
# # Returns the index of the first occurrence of a value.

 
t = (10, 20, 30, 20)
print(t.index(20))  # Output: 1
# ✅ Type Conversion (extra tricks):
# Although these are not methods on tuples, you can:

# 🔁 Convert tuple to list to modify:
 
t = (1, 2, 3)
temp = list(t)
temp.append(4)
t = tuple(temp)
print(t)  # (1, 2, 3, 4)

t = (10, 20, 30)
a, b, c = t
print(a, b, c)  # 10 20 30
# Summary of Tuple Methods:
# Method	Description
# .count(x)	Count occurrences of x
# .index(x)	Find first index of x


# there is three way to write the tuples
# a=()  # this called empty tupel
# a=(1,) #this is one elment tuple comma is need 
# a=(1,2,3,4,)#thius is multi tuple elemnt 