# Prompt the user to enter their points for the tests and main exam
test1 = int(input("Enter your points for Test 1 (out of 25): "))
test2 = int(input("Enter your points for Test 2 (out of 25): "))
main_exam = int(input("Enter your points for the Main Exam (out of 50): "))

# Calculate the total points
total_points = test1 + test2 + main_exam

# Check if the student passed the class and determine the grade
if total_points >= 50 and main_exam >= 25:
    if total_points > 80:
        print("Distinction")
    elif total_points > 60:
        print("Credit")
    else:
        print("Pass")
else:
    print("Fail")
