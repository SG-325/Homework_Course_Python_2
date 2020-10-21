import os

base_dir = os.getcwd()

os.makedirs("Dir1/Dir3/Dir4")
os.mkdir(f"{base_dir}/Dir1/Dir2")



while True:
	a = input("Do you want to delete folders? ")
	if a.lower() == "yes" or a.lower() == "no":
		break



list_cwd = os.listdir()

if a.lower() == "yes":
	while len(list_cwd) != 1:
		i = 0

		while True:
			list_cwd = os.listdir()

			if os.path.isfile(list_cwd[i]) and list_cwd[i] != "home_7.py":
				os.remove(list_cwd[i])
				break

			elif list_cwd[i] == "home_7.py":
				i += 1


			if os.path.isdir(list_cwd[i]):
				try:
					os.rmdir(list_cwd[i])
					break

				except Exception:
					os.chdir(list_cwd[i])
				

		os.chdir(base_dir)
		list_cwd = os.listdir()


	print("I did it.")

else:
	print("Goodbye!!!")