# write a program  find out the whether a student has pass or failed it requires a tootalk 40  and least 33%  in 
# each subject to pass assume 3 subjects  input bye UserWarning
# Input marks for 3 subjects
sub1 = int(input("Enter marks for Subject 1 (out of 100): "))
sub2 = int(input("Enter marks for Subject 2 (out of 100): "))
sub3 = int(input("Enter marks for Subject 3 (out of 100): "))

# Calculate total and percentage
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

# Check pass/fail conditions
if sub1 >= 33 and sub2 >= 33 and sub3 >= 33 and percentage >= 40:
    print("✅ Student has PASSED with", percentage, "%")
else:
    print("❌ Student has FAILED with", percentage, "%")
