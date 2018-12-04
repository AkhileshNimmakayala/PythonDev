# Accept month and display number of days
month = int(input("Enter a month[1-12]: "))
# if to take only a valid month between 1 and 12
if month <= 12:
    if month == 2:
        year = int(input("Enter the year:"))
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            days = 29
        else:
            days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    else:
        days = 31

    print("Number of days = ", days)

else:
    print("Not a valid month")
