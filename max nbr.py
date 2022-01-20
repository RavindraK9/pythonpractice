#wap to accept 3 numbers and find max number.



num1=10
num2=14
num3=18
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))
if(num1>=num2) and (num1>=num3):
   print("largest num=num1:")
elif(num2>num1) and (num2>num3):
    print("largest num=num2:")
else:
    print("largest num=num3:")
    