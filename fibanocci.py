#fibanocci series
n=int(input("enter n value:"))
n1=0
n2=1
if n==1:
    print(n1)
else:
    print(n1)
    print(n2)
    for i in range(2,n):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)