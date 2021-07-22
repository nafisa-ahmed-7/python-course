#Input from User : Name
#Reverse the Name
#Print reverse name


user_input = input("Enter a name: \n")
def rev(user_input):
    return user_input [::-1]
print("The reverse of the name: " + user_input + " is " ,rev(user_input))

#String Functions: .upper, .lower