user_input_1 = int(input("Enter a value :"))
user_input_2 = int(input("Enter a value :"))
user_input_3 = int(input("Enter a value :"))

#highest number
print("The highest of the three is" ,max(user_input_1,user_input_2,user_input_3))

#lowest number
print("The lowest of the three is" ,min(user_input_1,user_input_2,user_input_3))
list=[user_input_1,user_input_2,user_input_3]

#sum of three numbers
Sum=sum(list)
print("The sum of three numbers is",Sum)

#average of three numbers
import statistics
Average = statistics.mean(list)
print("The average of three numbers is" ,Average)

#squares of three numbers
Sq1=pow(user_input_1,2)
Sq2=pow(user_input_2,2)
Sq3=pow(user_input_3,2)
print("The square of user_input_1 is" ,Sq1)
print("The square of user_input_2 is" ,Sq2)
print("The square of user_input_3 is" ,Sq3)


