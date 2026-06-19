Run = int(input("Enter the total Run made by team:"))
Over = float(input("Enter the Over:"))
Ball = int(input("Enter the Balls:"))

Total_Balls =(Over * 6 )+Ball
Total_Over =Over+(Ball/6)
Run_Rate = Run/Total_Over

print("Total Over Balls : ", Total_Balls)
print("Total Run Rates :", Run_Rate)
