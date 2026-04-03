# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

student_score = 185
if student_score >= 101:
    print("Please verify your grade again")
    exit()

# if student_score < 60:
#     print("Grade F")
# elif student_score < 70:
#     print("Grade D")
# elif student_score < 80:
#     print("Grade C")
# elif student_score < 90:
#     print("Grade B")
# else:
#     print("Grade A")

if student_score >= 90:
    print("Grade A")
elif student_score >= 80:
    print("Grade B")    
elif student_score >= 70:
    print("Grade C") 
elif student_score >= 60:
    print("Grade D")
else:
    print("Grade F")         