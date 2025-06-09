# Relational Operators (Comparison Operators)
# Used to compare values. The result is always True or False.
# | Operator | Description           | Example (`a = 10, b = 5`) | Output |
# | -------- | --------------------- | ------------------------- | ------ |
# | `==`     | Equal to              | `a == b`                  | False  |
# | `!=`     | Not equal to          | `a != b`                  | True   |
# | `>`      | Greater than          | `a > b`                   | True   |
# | `<`      | Less than             | `a < b`                   | False  |
# | `>=`     | Greater than or equal | `a >= b`                  | True   |
# | `<=`     | Less than or equal    | `a <= b`                  | False  |

# Logical Operators
# Used to combine multiple conditions.
# | Operator | Description                            | Example            | Output |
# | -------- | -------------------------------------- | ------------------ | ------ |
# | `and`    | True if both conditions are true       | `a > 5 and b < 10` | True   |
# | `or`     | True if at least one condition is true | `a < 5 or b < 10`  | True   |
# | `not`    | Reverses the result                    | `not(a > 5)`       | False  |

a = 10
b = 5

# Relational
print(a == b)   # False
print(a != b)   # True
print(a > b)    # True

# Logical
print(a > 5 and b < 10)   # True
print(a < 5 or b < 10)    # True
print(not (a > 5))        # False
 
#   if-else and elif
# 🔹 if, elif, else – Conditional Statements in Python
# These are used to control the flow of your program based on conditions.


# if condition1:
#     # code block if condition1 is true
# elif condition2:
#     # code block if condition2 is true
# else:
#     # code block if none of the above are true

# 🔸 Explanation:
# if: Checks the first condition.

# elif (else if): Checks the next condition if the if was False.

# else: Runs if none of the conditions are True.

#   Example

age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
#  example 
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")
