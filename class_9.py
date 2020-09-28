

#1
# my_tuple = ("bmw", "mersedes", "2310", False, 5, 6)
# d = ""
# for i in my_tuple:
# 	d += str(i)

# print(d)

#2
# my_tup = ["1", "2", "5", "9", "5", "1", "6", "5", "9", "5"]
# s = 0
# for i in my_tup:
# 	if i.isdigit() and int(i) > 5:
# 		s += int(i)
# print("s = ", s)

#3
# def func(l:list) -> int:
# 	s = 0
# 	for i in l:
# 		if i % 2 == 0:
# 			s += i
# 	return s

# l  = [1, 2, 3, 5, 6, 4, 5, 6]
# print(func(l))

#4
my_list_1 = [1, 2, 3, 5, 7]

my_list_2 = my_list_1
print(my_list_1 is my_list_2)


my_list_2 = my_list_1.copy()
print(my_list_1 is my_list_2)



