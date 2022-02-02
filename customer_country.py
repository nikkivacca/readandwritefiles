
import csv
from operator import delitem 

customers = open('customers.csv','r')

customer_file = csv.reader(customers, delimiter=',')
next (customer_file)

outfile = open('customer_country.csv', 'w')

outfile.write('First Name, Last Name, Country' + '\n')
count = 0 

for record in customer_file:
    outfile.write(record[1]+ ',' + record[2] + ',' + record[4] +'\n')
    count+=1

print(count)

outfile.close()