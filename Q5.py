Salary = int(input("Enter your Salary:"))
Working_days = int(input("Enter the Number of Working Days:"))
Working_hours_per_day= int(input("Enter the Number of Working Hours:"))

Salary_per_day = Salary/Working_days
Salary_per_hour = Salary_per_day/Working_hours_per_day

print("Salary of per day :",Salary_per_day)
print("Salary of per hour :",Salary_per_hour)