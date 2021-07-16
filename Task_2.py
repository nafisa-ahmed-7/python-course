year = int(input("Enter a year: "))

if (year % 4) == 0:
    print(format(year)+" is a leap year")
else:
   print(format(year)+" is not a leap year")
