
class Temperature:

	def __init__(self, name_num):
		self.name = "home_"	+ str(name_num)
	


	def weather_type(self):

		while True:
			print(f"\n{self.name}:")
			temp = input("\tTell me the weather is hot or cold now? ")
			
			if temp.lower() == "hot" or temp.lower() == "cold":
				break

			print("You were input something wrong. Please try again.")


		if temp.lower() == "hot":
			self.goal_temp_1 = 23
			self.goal_temp_2 = 25

		else:
			self.goal_temp_1 = 22
			self.goal_temp_2 = 24




	def get_temp(self):
		t = f"{self.goal_temp_1} - {self.goal_temp_2} °C"
		return self.current_temp, t




	def set_temp(self, new_temp = "a"):
		if new_temp == "a":
			
			while True:
			
				try:
					new_temp = int(input("\n\tTell me the current temperature of your house. "))
					break

				except ValueError:
					print("You were input something wrong. Please try again.")

		self.current_temp = new_temp




	def __bool__(self):
		if self.current_temp >= self.goal_temp_1 and self.current_temp <= self.goal_temp_2:
			return True
		
		else:
			return False




	def __eq__(self, other):
		if self.goal_temp_1 == other.goal_temp_1 and self.current_temp == other.current_temp:
			return True

		else:
			return False




	def __ne__(self, other):
		if self.name != other.name:
			return True

		else:
			return False




	def __add__(self, other):
		t = self.name + other.name
		return t




#=================================================================================================================




def check_obj_temp(l):
	l_1 = []

	for i in l:
		if bool(i):
			l_1.append(i)

	if len(l_1) > 0:
		print(f"\nWe have {len(l_1)} house with a normal temperature.")
		
		for i in l_1:
			print("\t", i.name)

	else:
		print(f"\nWe don't have a house with a normal temperatures.")




#=================================================================================================================



while True:
	try:
		num = int(input("\nTell me the number of houses. "))
		
		if num < 1:
			raise TypeError("The number must be a possitive.")

		break

	except ValueError:
		print("You were input something wrong. Please try again.")
	
	except TypeError as t:
		print(t)




home_list = []

for i in range(1, num+1):
	h = Temperature(i)
	h.weather_type()
	h.set_temp()
	home_list.append(h) 




print("\n\nDescription of house temperature.")

for i in home_list:
	a, b = i.get_temp()
	print(f"\n\tThe current temperature of {i.name} is {a} °C")
	print(f"\tThe goal temperature of {i.name} is {b}")



check_obj_temp(home_list)


print("\nComparison of temperatures.")

l = []

for i in home_list:
	
	for j in home_list:
	
		if i != j and i == j and (i + j) not in l and (j + i) not in l:
			print(f"\t{i.name} and {j.name} have the same temperature.")
			l.append(i + j)


if len(l) == 0:
	
	if len(home_list) > 1:
		print("\tThe temperatures in the houses were different.")

	else:
		print("\tI have the temperature of one house.")

