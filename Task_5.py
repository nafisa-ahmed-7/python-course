#user input a string
user_input = str(input("Enter a value :"))
print(user_input)

#a.number of characters in the input
print("Number of characters in the string is" ,len(user_input))

#b.reverse the string
def reverse(value):
    return value[::-1]
value=user_input
print("The reverse of the string is",reverse(value))

#c.Find the uppercase letters
def uppercase(s):
    temp = ""
    for char in s:
        if char.isupper():
            temp=temp+char
    return temp
s=user_input
print("The uppercase letters in the string are :" ,uppercase(s))

#Find the lowercase letters
def lowercase(t):
    temp = ""
    for char in t:
        if char.islower():
            temp=temp+char
    return temp
t=user_input
print("The lowercase letters in the string are :" ,lowercase(t))

#d.Convert the string to uppercase and lowercase letters
print(user_input.upper())
print(user_input.lower())
