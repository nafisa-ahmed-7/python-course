import random
#Generate 100 random numbers between 1 and 1000
list_1 = random.sample(range(1, 1000), 100)
list_2=[]
list_3=[]
for num in list_1:
    if num % 2 == 0:
        list_2.append(num)
    else:
        list_3.append(num)
#Find number of even and odd numbers from the list and print them.
print("List of even number: ", list_2)
print("List of odd number: ", list_3)