import csv

students = open('student_scores.csv', 'r')

student_file = csv.reader(students, delimiter= ',')

outfile = open('student_avg.csv', 'w')

for student in student_file:
    grade_1 = float(student[1])
    grade_2 = float(student[2])
    grade_3 = float(student[3])
    average = (grade_1 + grade_2 + grade_3) / len(student)
    outfile.write(student[0] + ' ' + str(average) +'\n')

