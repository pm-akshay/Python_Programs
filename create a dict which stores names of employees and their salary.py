#pgm to create a dictionary which stores names of the employee and their salary
num=int(input('Enter the number of employees:'))
count=1
employee=dict()
while count<=num:
    name=input('Enter the name of the employee:')
    salary=int(input('Enter the salary:'))
    employee[name]=salary
    count+=1
print('\n\nEMPLOYEE_NAME\tSALARY')
for k in employee:
    print(k,'\t\t',employee[k])
