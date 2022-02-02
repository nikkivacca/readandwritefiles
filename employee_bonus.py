import csv
from operator import delitem 

employee = open('employeepay.csv','r')

employee_file = csv.reader(employee, delimiter=',')
next (employee_file)

for record in employee_file:
    bonus = float(record[4]) * float(record[3])
    total_pay = float(bonus) + float(record[3])
    print('First Name:' + record[1] )
    print('Last Name:' + record[2] )
    print('Salary: $' + record[3] )
    print('Bonus: $' + format(bonus,'.2f'))
    print('Total Pay: $' + format(total_pay, '.2f') + '\n')

