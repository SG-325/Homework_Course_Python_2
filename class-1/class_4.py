#1
# my_number = int(input("Enter a number!"))
# a = my_number % 2 
# print("It is even", a == 0)
# print("It is odd", a != 0)


my_number = int(input("Enter a number!"))
if my_number%2 == 0:
	print("It is even")
else:
	print("It is odd")



#2
# c = input("Tel me today's weather (raning, shining):")
# if c == "raning":
# 	print("Take an umbrella.")
# elif c == "shining":
# 	print("Take your sunglasses.")
# else:
# 	print("Do what you do.")
# print("I want to help you.")


#3
a = int(input("First number:"))
b = int(input("Second number:"))
c = int(input("Thirth number:"))
# if a>b and a>c:
#	print("Max value is a =", a)

if a > b:
	if a > c:
		print("Max value is a =", a)
	else:
		print("Max value is b =", c)
elif b > c:
		print("Max value is b =", b)
else:
	print("Max value is b =", c)





