#user input a string
user_input = str(input("Enter a value :"))
print(user_input)

#a.number of characters in the input
print("Number of characters in the string is" ,len(user_input))

#b.reverse the string
reverse_name = user_input [::-1]
print("The reverse of the name: " + user_input + " is " + reverse_name)

#c.Find uppercase and lowercase letters
print(user_input.isupper())
print(user_input.islower())

#d.Convert the string to uppercase and lowercase letters
print(user_input.upper())
print(user_input.lower())
