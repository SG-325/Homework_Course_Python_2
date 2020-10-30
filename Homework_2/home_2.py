from random import randint

class Mix:	
	def __init__(self, str_dict = ""):
		while len(str_dict) < 1:
			str_dict = input("\nTell me a sample string. ")

		len_str = len(str_dict)
		dic = {}
		
		for i in str_dict:
			dic.update({i : randint(1,len_str)})
		
		self.str_dict = dic



	def remove_duplicate(self):
		d = {}
		
		for i in self.str_dict:
			if self.str_dict[i] not in d.values():
				d.update({i : self.str_dict[i]})

		self.str_dict = d


	# nlargest()
	def max_values(self):
		list_values = list(self.str_dict.values())
		list_values.sort()


		# list_values.sort(reverse = True)
		# print(list_values[:3])


		if len(list_values) < 3:
			count = len(list_values)
		else:
			count = 3

		print("\nThe highest dictionary values.\n\t", end=" ")

		for i in range(len(list_values),len(list_values)-count,-1):
			print(list_values[i-1], end=" ")



my_obj = Mix()
print("\nCreated dictionary from the string.\n\t", my_obj.str_dict)

my_obj.remove_duplicate()
print("\nDictionary without duplicate values.\n\t", my_obj.str_dict)

my_obj.max_values()