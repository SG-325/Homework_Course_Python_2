#1
# text = input("Enter a word: ")
# if text[-3:] == "ing":
# 	t = text[:len(text)-3] + "ly"
# 	print(t)

#2
# word = "playing"
# c = input("leter: ")
# a = word.find(c)
# if c in word:
# 	word = word[:a] + "0" + word[a+1:]
# 	print("The word has changed ", word)
# else:
# 	print("The word hasn't changed ", word)

#3
# a = input("Enter somting: ")

# if a.isalpha():
# 	print("It's a string ", a)
# elif a.isdigit():
# 	print("It's a number ", a)
# else:
# 	q = a.find("0")
# 	n = int(input("Tell me a number: "))
# 	n += int(a[q])
# 	print("n = ", n)

#4
# t1 = "My name is {fname}, I'm {age}".format(fname = "S", age = 5)
# t2 = "My name is {0}, I'm {1}".format("S", 5)
# t3 = "My name is {}, I'm {}".format("S", 5)
# print(t1, "\n",  t2, "\n", t3)


# name = input("name: ")
# print(f"it is a word {name}")

#5
# c = range(1, 100, 10)
# print(c)

# a = 1
# b = 5
# c = range(a, b + 1, a+1)
# print(c)

#6
print(ord("a"))
print(chr(97))




