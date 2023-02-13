'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv
CSV = 'employee_data.csv'

#open the file
infile = open(CSV, 'r', newline='')
reader = csv.reader(infile, delimiter=',')


#create an empty dictionary
empdata={}

#use a loop to iterate through the csv file
next(reader)
for row in reader:
    fname = row[1]
    lname = row[2]
    dept = row[3]
    title = row[4]
    salary = int(row[5])

    #check if the employee fits the search criteria
    if dept == 'Marketing' and title == 'CSR':
        print(f'Manager Name: {fname} {lname} Current Salary: $' + format(salary, ',.2f'))

        full_name = fname + ' ' + lname
        new_salary = salary * 1.1
        
        empdata[full_name] = {'New salary' : format(new_salary, ',.2f')}

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for ok, ov in empdata.items():
    for ik, iv in ov.items():
        print(f'Manager Name: {ik} New salary: ${iv}')

        

        
    




