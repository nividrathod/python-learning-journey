minutes = int(input("Enter time in minutes: "))
hours = minutes/60
print(f"Time in hours is {hours}")
remaining = minutes % 60

if remaining == 0:
    print("No minutes left. You are exactly at an hour.")
else:
    print(f"{60 - remaining} minutes are left until the next hour.")