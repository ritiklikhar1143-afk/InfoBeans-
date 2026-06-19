principle = float(input("Enter the Principal:"))
rate = float(input("Enter the Rate:"))
time = float(input("Enter the Time:"))
amount = principal *(1+rate/100)**time
print("Compound interest is :",amount)