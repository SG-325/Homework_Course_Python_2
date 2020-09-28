import random

#1
# for i in range(1,11):
# 	print("This is for", i)
# 	for j in range(1,11):
# 		print(f"{i} * {j} = {i*j}")
# 	print("\n")	


#2
# for i in range(1,11):
# 	print(i*str(i))
# 	if i==6:
# 		for j in range(5,0,-1):
# 			print(j * str(j))
# 		break

#3
# pas = input("Enter your password, which lenght greater that 8 and there must be '.'. \n")

# while len(pas) < 8 or pas.find(".") == -1:
# 	print("You enter wrong password. Please try again.\n")
# 	pas = input("Enter your password, which lenght greater that 8 and there must be '.'. \n")


# print("Your password is right. ", pas)

# #Second version

# while True:
# 	password = input("Tell me a password.\n")
# 	if len(password) >= 8:
# 		if "." in password:
# 			break

# print("It's right!")

#4

c = 0
i = 0
print("If you are bored enter 'q'.")
while True:
	num = random.randint(4, 6)
	t = input("\nTry to guess the number. ")
	if t == "q":
		break
	elif num == int(t):
		c +=1
	else:
		if c != 0:
			c -= 1
	i += 1

print(f"\nYou are try {i} times and you bonuses {c}")



