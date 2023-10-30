"""
The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F
"""

subj1 = int(input("Enter marks for subject 1: "))
subj2 = int(input("Enter marks for subject 2: "))
subj3 = int(input("Enter marks for subject 3: "))


average = (subj1 + subj2 + subj3) / 3
print(f"Average marks: {average:.2f}")

if 90 <= average <= 100:
    grade = "A"
elif 80 <= average < 90:
    grade = "B"
elif 70 <= average < 80:
    grade = "C"
elif 60 <= average < 70:
    grade = "D"
else:
    grade = "F"


print(f"Grade: {grade}")

