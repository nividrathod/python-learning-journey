from datetime import date

day = int(input("\nEnter your birth day: "))
month = int(input("Enter your birth month: "))
year = int(input("Enter your birth year: "))

birth_date = date(year, month, day)
today = date.today()

days_lived = (today - birth_date).days

print("\nYou have lived approximately", days_lived, "days.")