basic = int(input("Enter your salary in Ruppes: "))

hra = basic * 0.20
da = basic * 0.10
gross_salary = basic + hra + da

print(f"Your HRA Allowance is {hra}")
print(f"Your DA Allowance is {da}")
print(f"Your Gross Salary is {gross_salary}")