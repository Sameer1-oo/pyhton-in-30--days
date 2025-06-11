#  while loop 
# #  The while loop in Python is used to execute a block of code repeatedly as long as a condition is true.

# while condition:
#     # Code block to repeat
# As long as the condition is True, the code inside the loop will keep running.

# example 1: Count from 1 to 5

i = 1
while i <= 5:
    print(i)
    i += 1

    # Missing i += 1 will cause an infinite loop!
    # Example 2: Loop until user enters "exit"
   
    user_input = ""
while user_input != "exit":
    user_input = input("Type 'exit' to stop: ")

# continue in a while loop in Python
# The continue statement skips the current iteration of the loop and moves to the next iteration, without executing the remaining code inside the loop for that cycle.

