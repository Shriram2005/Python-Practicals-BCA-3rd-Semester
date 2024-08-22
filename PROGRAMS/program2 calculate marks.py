'''
Aim: WAP to calculate total marks, percentage and grade of a student. Marks obtained in each of the three subjects are to be input by the user.
Assign grades according to the following criteria:
Grade A: Percentage >=80
Grade B: Percentage>=70 and <80
Grade C: Percentage>=60 and <70
Grade D: Percentage>=40 and <60
Grade E: Percentage<40
'''

s1 = int(input("Enter marks in subject 1 : "))
s2 = int(input("Enter marks in subject 2 : "))
s3 = int(input("Enter marks in subject 3 : "))
s4 = int(input("Enter marks in subject 4 : "))
s5 = int(input("Enter marks in subject 5 : "))

total = s1 + s2 + s3+ s4 + s5
percentage = (total/500) * 100
grade = ''

if percentage  >= 80:
    grade = 'A'
elif percentage >= 70 and percentage < 80:
    grade = 'B'
elif percentage >= 60 and percentage < 70:
    grade = 'C'
elif percentage >= 40 and percentage < 60:
    grade = 'D'
else:
    grade = 'E'

print(f"Total marks : {total}\nPercentage : {percentage}\nGrade : {grade}")