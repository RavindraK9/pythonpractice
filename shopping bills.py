#WAP to accept salary and 3 shopping bills from user and find
# 1. total shoppping amount
# 2. find how much % of amount he/she spent on shopping on his salary.

salary=float(input("enter your salary :"))
shoppingbill1=float(input("enter shopping bill 1 :"))
shoppingbill2=float(input("enter shopping bill 2 :"))
shoppingbill3=float(input("enter shopping bill 3 :"))

total=shoppingbill1+shoppingbill2+shoppingbill3

salaryspent=(total*100/salary)

print("total shopping amount :", total)
print("percentage :", salaryspent)
