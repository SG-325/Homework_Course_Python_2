from random import randint as r

check = "yes"
while check.lower() == "yes":
	random_number = str(r(1000,9999))
	print("\nrandom number =", random_number)
	count = 0

	while True:
		p = 0
		while p == 0:
			try:
				user_choice = input("\nGuess the 4-digit number.")
				if not user_choice.isdigit():
					raise ValueError(f"{user_choice} is not a digit or integer. Try again.")
				if len(user_choice) != 4:
					raise TypeError(f"Length of {user_choice} isn't equal 4. Try again.")
				p = 1

			except ValueError as v:
				print(v)
				
			except TypeError as t:
				print(t)


		bulls = 0
		cows = 0
		for i in range(4):
			if random_number[i] in user_choice:
				bulls += 1
				if random_number[i] == user_choice[i]:
					cows += 1
				
		bulls = bulls - cows
		count += 1

		if cows == 4:
			print(f"You have ({cows} cows, {bulls} bulls).")
			print("\nYou won!!!")
			break
		else:
			print(f"For this time you have ({cows} cows, {bulls} bulls).")

	print(f"You tried to guess {count} time.")
	check = input("\nIf you want to continue the game enter 'yes'. Otherwise enter 'no'.")






