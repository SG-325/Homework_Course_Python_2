#1
# n = int(input("Enter a number: "))

# for i in range(1,10):
# 	print(f"{n} x {i} = {n*i}")

#2
# y = input("Enter a number: ")

# s = 0
# for i in y:
# 	s += int(i) 
# print("Sum = ", s)

#3
# num = input("Enter a text: ")

# s = 0
# for i in num:
# 	if i.isdigit():
# 		s += int(i)
# print("Sum = ", s)

#4
# s = 0
# for i in range(1,21):
# 	s += i

# for i in range(1,21):
# 	if i % 3 != 0:
# 		continue
# 	else:
# 		s -= i

# print("s = ", s) 

#5
s = 0
j = 15
for i in range(1,21):
	s += i
	if s >= j:
		break

print("s = ", s)

a = s - i

if j - a > s - j:
	print("s = ", s)
else:
	print("s = ", a)






