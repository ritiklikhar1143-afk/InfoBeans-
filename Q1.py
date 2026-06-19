price = float(input("Enter the total amount : "))
gst = float(input("Enter the gst :"))
s_charge = float(input("Enter the service charge :"))
Num_of_Friends = float(input("Enter the Number of Friend:"))

gst = float((price*gst)/100)
s_charge = float((price*s_charge)/100)
F_Bill = price+gst+s_charge
split = F_Bill/Num_of_Friends

print(split)