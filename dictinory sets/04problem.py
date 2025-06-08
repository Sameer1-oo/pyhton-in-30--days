# can yopu can chage the value inside the set  wghich is coantain a set 
s1 = {1, 2, 3}
s2 = {4, 5, s1}  # ❌ This gives: TypeError: unhashable type: 'set'


# example
s1 = frozenset([1, 2, 3])
s2 = {s1, 4, 5}
print(s2)  # Output: {frozenset({1, 2, 3}), 4, 5}

#  You cannot store a set inside another set.
# Why?
# Because sets are unhashable and mutable, so they can't be elements of another set.

