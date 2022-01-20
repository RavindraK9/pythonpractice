#wap to accept project marks, internal marks and externaks and find total marks
#total_marks= 70% from project+20% from external +10% from internal

project_marks=int(input("enter your project_marks :"))
external_marks=int(input("enter your external_marks :"))
internal_marks=int(input("enter your internal_marks :"))

total_marks=(project_marks*70/100)+(external_marks*20/100)+(internal_marks*10/100)
print("total_marks :",total_marks)