#import palindrome_check

#var = "abcba"
#palindrome_check.check_palindrome(var)

def extract_digits(user_input):
    digits_list =[]
    while (user_input>0):
        digits_list.append((user_input%10))
        user_input=int(user_input/10)
    return digits_list

def list_sum(digits):
    total = 0
    for each_elem in digits:
        #total=total+each_elem
        total+=each_elem
    return total

user_input = int(input("Enter a number: "))
digits = extract_digits(user_input)
final_sum = list_sum(digits)
print("Sum of all elements of number "+ str(user_input) + " is " + str(final_sum))