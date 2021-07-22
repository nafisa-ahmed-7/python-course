#class1.txt (input , function description, output) start with class 2
#sample - reverse name
'''
Task - To reverse a name given by user input
user input: "user input"
reverse name: ...output
'''

import os

curr_working_dir = os.getcwd()

f = open('class2a.txt', 'w')
from reverse_name import rev, user_input
f.write("This is a function to reverse a given string\n")
f.write(rev(user_input))
f.close()

f = open("class2a.txt","r")
file_content = f.read()
output=rev(user_input)
f.close()
print(output)