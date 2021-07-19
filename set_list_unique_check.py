#user_input a list of numbers. Check if all numbers are unique.

user_input = x=list(map(int,input("Enter the numbers:\n").split(" ")))
if len(user_input) == len(set(user_input)):
    print("All numbers are unique")
else:
    print("not unique")


'''
Task1: user input the birthdate Not hardcode
Task 5: uppercase, lowercase print characters. Not true false. Try to define string reverse func on your own.
Task 4: write the functions on your own. Convert 3 inputs to a generic user input so that it works with any no of elements
Task 3: write a func for num validation to be used by other files
Set theory:
a. create a set , b. add members to a set, c. print all elements one by one d. remove an item if present e. union, intersection , difference of 2 sets.
f. Check if one set is subset of another set. g. max, min in set

Breakdown an user input amount (a number) into denominators of currency. (500,200,100,50,20,10,5,2,1). 
2678 - 2678/500 = 5. 2678%500 = 178/200 = 0 - 178/100=1. 178%100=78. 
'''