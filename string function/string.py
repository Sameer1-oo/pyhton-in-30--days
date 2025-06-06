# string is data type .
# string is sequnce of chacter  enclosed in qouts .
# we can write string in 3 ways 
a='sameer'
b="sameer"
c=''' sameer ''' 
# this use for multi line string .

#   string is immutable once you c reate a sting that nevr b change . We can change only using string function 
name = "sameer"
#  indexing strat from 0  santax to write slicing in string examole ::: string[ind__sart : ind__end]
# rember thge last index not included
nameshort = name[1:3]
print(nameshort)

# there is many type of function in string .
# string function 
# In Python, string functions (also called string methods) are built-in methods used to manipulate or analyze strings. Here's a list of the most commonly used string functions with examples:

# 🔹 Basic String Functions
# Function	Description	Example
# len()	Returns the length of a string	len("Hello") → 5
# str()	Converts a value to a string	str(123) → "123"

# 🔹 String Case Functions
# Function	Description	Example
# upper()	Converts all characters to uppercase	"hello".upper() → "HELLO"
# lower()	Converts all characters to lowercase	"HELLO".lower() → "hello"
# title()	Capitalizes the first letter of each word	"hello world".title() → "Hello World"
# capitalize()	Capitalizes the first character	"hello".capitalize() → "Hello"
# swapcase()	Swaps case of each character	"HeLLo".swapcase() → "hEllO"

# 🔹 Searching & Checking
# Function	Description	Example
# find()	Returns index of first match or -1	"hello".find("e") → 1
# index()	Same as find(), but gives error if not found	"hello".index("l") → 2
# startswith()	Checks if string starts with value	"hello".startswith("he") → True
# endswith()	Checks if string ends with value	"hello".endswith("o") → True
# in	Checks if substring exists	"e" in "hello" → True

# 🔹 Modifying Strings
# Function	Description	Example
# replace()	Replaces part of the string	"hello".replace("l", "x") → "hexxo"
# strip()	Removes whitespace from both sides	" hello ".strip() → "hello"
# lstrip()	Removes whitespace from left	" hello".lstrip() → "hello"
# rstrip()	Removes whitespace from right	"hello ".rstrip() → "hello"
# split()	Splits string into a list	"a,b,c".split(",") → ["a", "b", "c"]
# join()	Joins list into a string	" ".join(["Hi", "there"]) → "Hi there"

# 🔹 String Validation
# Function	Description	Example
# isalpha()	True if all characters are letters	"abc".isalpha() → True
# isdigit()	True if all characters are digits	"123".isdigit() → True
# isalnum()	True if all characters are letters or digits	"abc123".isalnum() → True
# isspace()	True if all characters are whitespace	" ".isspace() → True
# islower()	True if all letters are lowercase	"hello".islower() → True
# isupper()	True if all letters are uppercase	"HELLO".isupper() → True

# they are the are the str5ing function 
 
#  example
lenth = "sameer"
print(len(lenth))

# example
sameer = "sameer good boy "
print(sameer.replace("good","very handsome"))
#  example
