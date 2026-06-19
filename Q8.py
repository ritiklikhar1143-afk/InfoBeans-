Distance = int(input("Enter the Distance:"))
Mileage = int(input("Enter the Mileage:"))
Fuel_price = float(input("Enter the exact price of fuel:")) 

Fuel_Cons = Distance /Mileage
Cost = Fuel_Cons*Fuel_price

print("Fuel Consumed :",Fuel_Cons)
print("Total Cost :",Cost)