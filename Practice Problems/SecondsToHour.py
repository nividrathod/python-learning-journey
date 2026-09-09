seconds = int(input("Enter time in seconds: "))

minutes = seconds/60
hours = seconds/3600

print(f"Time in minutes is {minutes}")
print(f"Time in hours is {hours}")

if seconds % 3600 != 0:
    remaining = 3600 - (seconds % 3600)
    print(f"Remaining seconds to complete an hour is {remaining}")