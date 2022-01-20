#wap to accept units from user and find the bill.
#for first 50 units the charge are : 0.75p/u
#next 100 units the charge are : 2.10p/u
#next 100 units the charge are : 2.50 p/u
#next 250 units the charge are : 2.80p/u

units=int(input("enter the unit value:"))
bill=0
if units<=50:
    bill=0.75*units;
elif units<=150:
    bill=(50*0.75)+(units-50)*2.10
elif units<=250:
    bill=(50*0.75)+(100*2.10)+(units-150)*2.50
else:
    bill=(50*0.75)+(100*2.10)+(units-250)*2.80
    
#adding 10% GST to the bill
print("bill:",bill)
gst=(bill*10)/100
bill=bill+gst
print("gst:",gst)
print("final bill:",bill)