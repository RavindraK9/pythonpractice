#WAP to accept basic salary and find gross salary
#gross salary=basic+HRA+DA
da is 80% on basic
hra is 76% on basic




basicsalary=float(input("enter basic salary :",))
da=(basicsalary*80/100)
hra=(basicsalary*76/100)

gross_salary=basicsalary+da+hra
print("gross salary:",gross_salary)