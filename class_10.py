#1

# number = input("Tell me a number. ")
# try:
# 	half = int(number)/2
# except ValueError:
# 	print("The Value of number is not int.")

# num_1 = input("\nTell me a number to divide 4 with.")

# try:
# 	new_value = 4/int(num_1)
# except ZeroDivisionError:
# 	print("The num_1 can not be 0")
# except ValueError:
# 	print("The Value of number is not int.")

# num = int(input("\nTell me a number."))

# try:
# 	num = num + "2"
# except TypeError:
# 	print("You cann't use int and str.")

# my_list = [1, 2, "hello"]
# try:
# 	print(my_list[3])
# except IndexError:
# 	print("\nThere isn't that index")

# try:
# 	print(Hello)
# except NameError:
# 	print("At first define Hello")



#2
# my_num = input("Tell me a number. ")
# my_list = [1, 2, "hello"]

# try:
# 	print(int(my_num)/2)
# 	print(4/int(my_num))
# 	print(my_num + "2")
# 	print(my_list[3])
# 	print(a)
# except ValueError:
#  	print("The Value of number is not int.")
# except ZeroDivisionError:
#  	print("The num_1 can not be 0")
# except TypeError:
#  	print("You cann't use int and str.")
# except IndexError:
#  	print("\nThere isn't that index")
# except NameError:
#  	print("At first define a")



#3 ====================Password====================

check = True
while check:
	try:
		password = input("Tell me your Password.")
		
		if len(password) < 8:
			raise ValueError("It should be greather than 8.")
		
		check_ = False
		for i in password:
			if  i.isdigit():
				check_ = True
			if not i.isalpha():
				if i != " ":
					break
				else:
					raise NameError("The password could not contain a space.")
			
		if not check_:
			raise TypeError("Should contain at least one number.")

		if password[0].islower():
			raise Exception("Should start with a capital letter.")
		check = False
	except ValueError as e:
		print(e)
	except NameError as n:
		print(n)
	except TypeError as t:
		print(t)
	except Exception as ex:
		print(ex)

print(F"{password} is a strong one, thanks!!!")



