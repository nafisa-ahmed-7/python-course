user_input = input("Enter a value :\n")
if user_input.isdigit() :
    print("It is a number")
    user_input=int(user_input)
    if user_input%2==0:
        print("Yes")
    else:
        print("No")
else:
    print("Please retry")



