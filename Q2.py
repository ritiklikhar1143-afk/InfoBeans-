Smartphone = int(input("enter the amount of the Smartphone:"))
Downpayment = int(input("Enter the Downpayment you made:"))
Interest = int(input("Enter the Interest rate: "))
Months = int(input("Enter the Number of the Months: "))

Remaining_Amount = Smartphone-Downpayment
Total_with_interest = Smartphone + Smartphone*(Interest/100)
Monthly_EMI = Total_with_interest/Months

print("Remaining Amount is:",Remaining_Amount)
print("Total Amount with Interest is:",Total_with_interest)
print("Monthly EMI is:",Monthly_EMI)