#User input 2 dates. Find their difference.

import datetime
f_date_year = input("\nEnter 1st year: ")
f_date_month = input("\n Enter 1st month: ")
f_date_date = input("\n Enter 1st day: ")
f_date = datetime.date(int(f_date_year),int(f_date_month),int(f_date_date))
print("First date is " + str(f_date))


l_date = input("\nEnter 2nd ...")


diff = l_date-f_date
print("diff is "+ diff.days)

#current time = datetime.datetime.now()
#remainder = 19%5
#Tasks:
#1. Get a birthday and find the day of the week
#2. Input a year and print out if it is a leap year
#3. Input a number from user. Validate if it is a number. If not, tell user to retry. If number is even, print yes, else no.
#4. Input 3 numbers from user. Validation. Print the highest, lowest, their sum, average, squares.
#5. User input a string. a. Count number of characters in the string. b. Reverse the string. c. Find upper case letters and lowercase letters. d. Convert the string to upper and lower
#6. Find number of even and odd numbers from the list and print them.
#     numbers = [] initialise the list. Randomly insert 100 numbers between 1-1000.
#7. From the above list, print the 10th element.