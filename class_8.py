from random import randint
#1

# def birth():
# 	name = input("Tell me your name!")
# 	print("Happy birthday my dear", name)
# 	return name

# k = birth()
# print(k)

#2
# help(randint)
# print(randint.__doc__)

#3
# def func(a:str, b: str) -> str:
# 	pass

# print(func.__annotations__)

#4
# def f(i):
# 	if i <= 0:
# 		p = 1
# 	else:
# 		p = i*f(i-1)
# 	return p 


# i = int(input("Enter a number:"))
# print(f(i))

#5

# def s(a,c):
# 	if c==0:
# 		print("The second value couldn't be 0")
# 		return
# 	else:
# 		return int(a/c)

# print(s(11,5))



# 6
# def V(a,b,c=1):
# 	V = a * b * c
# 	return V

# a = int(input("a = "))
# b = int(input("b = "))
# c = input("c = ")
# if c == "":
# 	print(V(a, b))
# else:
# 	print(V(a, b, int(c)))


#7

# check = "y"
# user_score = 0
# computer_score = 0
# rounds = 0

# while check == "y":
# 	user_choice = int(input("Tell me, 1 for R, 2 for P, 3 for S:"))
# 	computer = randint(1,3)
# 	if (user_choice == 1 and computer==2) or (user_choice == 2 and computer==3) or (user_choice == 3 and computer==1):
# 		user_score += 1
# 	elif computer == user_choice:
# 		print("Tie")
# 	else:
# 		computer_score += 1
# 	rounds += 1
# 	check = ""
# 	while check != "y" and check != "n":
# 		check = input("Do you want to play again:y for yes, n for no:")

# print(f"Rounds {rounds}\nYuor scor is {user_score}\nComuter scor is {computer_score}")



