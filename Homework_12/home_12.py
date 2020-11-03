import sqlite3
from sqlite3 import Error
import json
import os


database = os.path.join("C:/Users/User/Desktop/Python_Basic_It/Course-2/Database", "film.db")

try:
	conn = sqlite3.connect(database)
except Error as e:
	print(e)

curs = conn.cursor()




#Task_1
print("Task_1\n")

name_B = """SELECT title 
			FROM film 
			WHERE title LIKE("B%")
		"""


for i in curs.execute(name_B):
	print("\t", i)




#Task_2
print("\nTask_2\n")

max_length = """SELECT title, max(length) AS Max 
				FROM film
			"""


for i in curs.execute(max_length):
	print("\t", i)




#Task_3
all_select = """SELECT * 
				FROM film 
				ORDER BY film_id
			"""


list_ = ["film_id", "title", "description", "release_year", "rate", "length", "special_features"]
dict_ = {}


for i in curs.execute(all_select):
	dict_try = {}

	for j in range(len(i)):
		dict_try.update({f"{list_[j]}":f"{i[j]}"})

	dict_.update({f"{i[0]}":dict_try})


with open("a.json","w") as f:
	json.dump(dict_, f, indent = 6)




#Task_4
filtered_film = """CREATE TABLE filtered_film 
					AS 
					SELECT * FROM film 
					WHERE release_year > 2010 
						AND rate BETWEEN 3 AND 5 
					ORDER BY film_id
				"""

curs.execute(filtered_film)
conn.commit() 
