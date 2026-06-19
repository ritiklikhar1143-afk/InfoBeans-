Seconds = int(input("Enter the Seconds  :"))
Hours = int(Seconds/3600)
remaining = Seconds%3600
minutes = int(remaining/60)
rem_seconds = minutes%60

print("Number of the Hours:",Hours)
print("Number of the Minutes:",minutes)
print("Number of Seconds:",rem_seconds)