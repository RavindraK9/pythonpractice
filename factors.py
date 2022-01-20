#wap to find factors of a given number
#wap number of factors of a given number

#x=int(input("enter the factors:"))
#for i in range(1, x+1):
 #   if x%i==0:
  #      print(i)
n=0
x=int(input("enter the factors:"))
for i in range(1, x+1):
   if x%i==0:
       n+=1
print("number of factors:",n)


 

