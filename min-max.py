def find_max(num_list):
    temp_max = num_list[0]
    for each_element in num_list:
        if each_element>temp_max:
            temp_max = each_element
    return temp_max

def find_min(num_list):
    temp_min = num_list[0]
    for each_element in num_list:
        if each_element<temp_min:
            temp_min=each_element
    return temp_min

def str_to_int(str_list):
    for i in range(len(str_list)):
        str_list[i] = int(str_list[i])
    return str_list

user_input = input("Enter a list of numbers separated by comma: ")
num_list = user_input.split(",")
num_list = str_to_int(num_list)
print("Max value of the list is " + find_max(num_list))
print("Min value of the list is " + find_min(num_list))