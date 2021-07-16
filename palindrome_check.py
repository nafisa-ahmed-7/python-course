def check_palindrome(variable):
    if variable == variable[::-1]:
        print(variable + " is a palindrome")
    else:
        print(variable + " is not a palindrome")

user_input = input("Enter a string: ")
check_palindrome(user_input)