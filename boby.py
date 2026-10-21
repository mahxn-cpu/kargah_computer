import os
os.system('cls')
year = int(input("Enter the year:"))
if year % 400 == 0:
    print("It's a leap year")
elif year % 100 == 0:
    print("It's not a leap year")
elif year % 4 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")
