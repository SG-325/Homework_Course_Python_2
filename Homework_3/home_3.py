from math import pi
from random import randint

#Task_1
print("\nTask_1")

class Circle(object):

	def __init__(self):
		while True:
			try:
				self.radius = int(input("\nTell me the radius of the circle."))
				break
			except ValueError:
				print("You must enter an integer.")


	def area(self):
		S = pi * self.radius**2
		return S


	def perimeter(self):
		P = 2 * pi * self.radius
		return P



circle_obj = Circle()

print(f"\nThe area of a circle with {circle_obj.radius} radius.\n\tS = {circle_obj.area()}")
print(f"\nThe perimeter of a circle with {circle_obj.radius} radius.\n\tP = {circle_obj.perimeter()}")


#Task_2
print("\n===============================================================================")
print("\nTask_2")

class Sum(object):

	def __init__(self, target = 50):
		self.target = target

		self.array = []

		for i in range(10):
			self.array.append(randint(10, 99))
			

	def sum_num(self):
		l = []

		for i in range(len(self.array)):
			for j in range(len(self.array)):
				
				if self.array[i] + self.array[j] == self.target:
					if [j,i] not in l:
						l.append([i,j])

		return l


	def printing(self, l):
		print("List:\n\t", self.array)

		if len(l) > 0:
			for i in l:
				print(F"\n{self.array[i[0]]} + {self.array[i[1]]} = {self.target}")
				print(F"{i[0]}    {i[1]}")
		
		else:
			print(F"There were no 2 numbers in the list, the sum of which is {self.target}.")



ob = Sum()
ob_list = ob.sum_num()
ob.printing(ob_list)


#Task_3
print("\n===============================================================================")
print("\nTask_3")

class Person(object):

	def __init__(self, name, surname, age, gender):
		self.name = name
		self.surname = surname
		self.gender = gender
		self.age = age
 

	def army(self):
		if self.gender == "male" and self.age >= 20:
			print("You have returned from the army.")
		else:
			print("You didn't go to the army.")



class Student(Person):

	def __init__(self, name, surname, age, gender, group, AQS):
		self.group = group
		self.AQS = AQS
		Person.__init__(self, name, surname, age, gender)


	def check_AQS(self):
		if self.AQS >= 81:
			print("Congratulations!!! You can study for free.")
		else:
			print("Oh no!!! You can't study for free.")



ob_1 = Student("Sara", "Connor", 20, "female", "H719", 95)
ob_2 = Student("John", "Smith", 23, "male", "H755", 75)

print("\nob_1:", ob_1.__dict__)
print("ob_2:", ob_2.__dict__)

print("\nob_1:")
ob_1.army()
ob_1.check_AQS()

print("\nob_2:")
ob_2.army()
ob_2.check_AQS()

