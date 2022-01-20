#wap to accept basic salary and find gross salary.
#gross_salary=basic+HRA=DA
#if basic salary <10000
#DA is 70% on basic
#HRA is 70% on basic
#basic salary is between 10000 to 20000
#DA is 75% on basic
#HRA is 73% on basic
#basic salary is above 20000
#DA is 80% on basic
#HRA is 76% on basic

basic_salary=int(input("enter basic_salary:"))
if basic_salary<10000:
    DA=(basic_salary*70)/100
    HRA=(basic_salary*70)/100
elif basic_salary>10000 and basic_salary<20000:
     DA=(basic_salary*75)/100
     HRA=(basic_salary*73)/100
else:
    DA=(basic_salary*80)/100
    HRA=(basic_salary*76)/100

gross_salary = basic_salary+DA+HRA
print("gross_salary:",gross_salary)
    

