speed = int(input("Enter the Speed :"))
hour = int(input("Enter hour:"))
minute = int(input("Enter the minutes:"))

total_time = hour + (minute/60)
distance = speed * total_time

print("total_time:",total_time)
print("Distance :",distance)
