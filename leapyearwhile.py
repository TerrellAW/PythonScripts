print("Leap Year Calculator")
year = int(input("Enter a Year: "))
while (year != 0):
    if year % 400 == 0 and year % 100 == 0 or year % 4 == 0:
        print(f"{year} is a leap year.")
        year = int(input("Enter a Year: "))
    else:
        print(f"{year} is not a leap year.")
        year = int(input("Enter a Year: "))
print("Invalid year.")
