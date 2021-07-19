user_input = input("Enter a value :\n")
def num_validation(k):
    if user_input.isdigit():
        print("Num verified")
    else:
        print("Please retry")
k=user_input
print(num_validation(k))

#odd_even numbers
user_input_1=int(input("Enter a number:\n"))
if user_input_1%2==0:
    print("Yes")
else:
    print("No")



