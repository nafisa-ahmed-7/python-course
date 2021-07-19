x=list(map(int,input("Enter the numbers:\n").split(" ")))
#highest number
def find_max(num_list):
    temp_max = num_list[0]
    for each_element in num_list:
        if each_element>temp_max:
            temp_max = each_element
    return temp_max
num_list=x
print("The maximum value from the given numbers:" ,find_max(num_list))

#lowest number

def find_min(num_list):
    temp_min = num_list[0]
    for each_element in num_list:
        if each_element<temp_min:
            temp_min=each_element
    return temp_min
num_list=x
print("The minimum value from the given numbers:" ,find_min(num_list))

#sum of three numbers
def sum(values):
    total = 0
    for s in values:
        total=total+s
    return total
values=x
print("The sum of the numbers" ,sum(values))

#average of three numbers
def Average(s): #num_list (for each_el in nu...)

    return sum(s) / len(s) #sum is python's func. use sth else. use your sum func.
s=x
print("The average of the numbers:" ,Average(s))

#square of the given number
def square_elem(x):
    z=int(input("Enter an element:\n"))
    k=z*z
    return k
print("The square of the element is:" ,(square_elem(x)))
