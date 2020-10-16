
class Hotel:
	def __init__(self, hotel_name, place, mid_room_price, lux_room_price):
		self.hotel_name = hotel_name
		self.place = place
		self.rooms_mid = {"r1":"free", "r2":"bussy", "r3":"free", "r4":"free", "r5":"free"}
		self.mid_room_price = mid_room_price
		self.rooms_lux = {"r1":"free", "r2":"free", "r3":"bussy", "r4":"free", "r5":"free"}
		self.lux_room_price = lux_room_price



	def presentation(self):
		text = F"We will stay {self.hotel_name} whitch offers two types of rooms middle {self.mid_room_price} and lux {self.lux_room_price}."
		return text



	def del_booking(self, key, room_type):
		if room_type.lower() == "middle":
			
			if (key in self.rooms_mid) and (self.rooms_mid[key] == "bussy"):
				self.rooms_mid[key] = "free"
				return 1
			
			else:
				return 0
		
		else:
			
			if (key in self.rooms_lux) and (self.rooms_lux[key] == "bussy"):
				self.rooms_lux[key] = "free"
				return 1
			
			else:
				return 0



	def booking(self, key, type_):
		if type_.lower() == "middle":
			self.rooms_mid[key] = "bussy"

		else:
			self.rooms_lux[key] = "bussy"



	def available_room_check(self, room_type):
		mid_free_rooms = []
		lux_free_rooms = []


		for i in self.rooms_mid:
			if self.rooms_mid[i] == "free":
				mid_free_rooms.append(i)

		for i in self.rooms_lux:
			if self.rooms_lux[i] == "free":
				lux_free_rooms.append(i)



		if room_type == "middle":
			k_1 = mid_free_rooms
			k_2 = lux_free_rooms
			second_type = "luxury"

		else:
			k_1 = lux_free_rooms
			k_2 = mid_free_rooms
			second_type = "middle"



		if len(k_1) > 0:
			print(f"\nFree {room_type} rooms numbers are: {k_1}")

			while True:
				try:
					key = input("\nTell me which room do you want?")
								
					if key not in k_1:
						raise ValueError("You were input something wrong. Please try again.")

					self.booking(key, room_type)
					return True

				except ValueError as v:
						print(v)
		
		
		elif len(k_2) > 0:
			print(f"\nNow we don't have free {room_type} rooms but we can offer {second_type} rooms.")
			
			while True:
				
				try:
					check = input(f"\nDo you want a {second_type} room? ")
					
					if check.lower() != "yes" and check.lower() != "no":
						raise ValueError("You were input something wrong. Please try again.")
				
				except ValueError as v:
					print(v)
					

				if check.lower() == "yes":
					print(f"\nFree {second_type} rooms numbers are: {k_2}")

					try:
						key = input("\nTell me which room do you want?")
							
						if key not in k_2:
							raise ValueError("You were input something wrong. Please try again.")

						self.booking(key, second_type)
						return True

					except ValueError as v:
						print(v)
				else:
					return False

		else:
			print("\nNow we don't have free middle or luxury rooms.")
			return False



	def discount(self, percent, room_type):
		if room_type == "middle":
			self.mid_room_price -= (self.mid_room_price * percent)/100

		else:
			self.lux_room_price -= (self.lux_room_price * percent)/100


#======================================================================================================================


class Taxi:
	def __init__(self, taxi_name, car_types, price_for_tour):
		self.taxi_name = taxi_name
		self.car_types = car_types
		self.price_for_tour = price_for_tour



	def presentation(self):
		text = F"which includes transport with {self.taxi_name} company whitch provides {self.car_types} and price for it is {self.price_for_tour}. "
		return text



	def discount(self, percent):
		self.price_for_tour -= (self.price_for_tour * percent)/100



#======================================================================================================================



class Tour(Hotel, Taxi):
	def __init__(self, name, hotel_name, place, mid_room_price, lux_room_price, taxi_name, car_types, price_for_tour):
		self.name = name
		
		Hotel.__init__(self, hotel_name, place, mid_room_price, lux_room_price)
		Taxi.__init__(self, taxi_name, car_types, price_for_tour)
		
		self.price_lux_tour = self.lux_room_price + self.price_for_tour
		self.price_mid_tour = self.mid_room_price + self.price_for_tour



	def presentation(self):
		text = F"Hello, we offer {self.name} tour. We have two options {self.price_lux_tour} and {self.price_mid_tour}, "
		text += Taxi.presentation(self) + Hotel.presentation(self)
		print(text)



	def discount(self, percent_1, percent_2, room):
		Hotel.discount(self, percent_2, room)
		Taxi.discount(self, percent_1)



	def price_printing(self):
		text = F"\n\tFor a middle room: {self.mid_room_price}\n\tFor a luxery room: {self.lux_room_price}\n\tFor a taxi: {self.price_for_tour}"
		print("\nPrices:", text)


#======================================================================================================================


ob = Tour("Dilijan", "Dilijan Garden House", "Dilijan", 20000, 50000, "ride_over", "mercedes", 10000)

ob.presentation()



while True:
	a = input("\nDo you want to take part in our tour? ")
	if a.lower() == "yes" or a.lower() == "no":
		break


if a.lower() == "yes":

	while True:
		room = input("\nWhat kind of room do you want middle or luxury? ")
		if room.lower() == "middle" or room.lower() == "luxury":
			break


	while True:
		status = input("\nTell me your status:\n\tStudent:(1)\n\tAge is less than 18:(2)\n\tYou are a newlywed:(3)\n\tOther:(4)\nStatus = ")
		if status in "1234":
			break

	if status in "123":
		percent_1 = 10
		percent_2 = 20
		print("\nCongratulations!!!\nYou can take the following discounts:\n\tFor a room:20%\n\tFor a taxi:10%")

		ob.discount(percent_1, percent_2, room)
		

	ob.price_printing()

	if ob.available_room_check(room.lower()):

		while True:
			a = input("\nHave you changed your mind? ")

			if not a.isalpha():
				continue
			
			if a.lower() == "yes" or a.lower() == "no":
				break


		if a.lower() == "yes":
			while True:
				
				try:
					rt = input("\nTell me the kind of your room. ")

					if rt.lower() != "middle" and rt.lower() != "luxury":
						raise ValueError("You were input something wrong. Please try again.")

				except ValueError as v:
					print(v)
					continue


				key = input("\nTell me number of your room.(r?) ")
				

				if ob.del_booking(key, rt) == 1:
					print("\nAll is okey. Thank you!")
					break

				else:
					print("\nSomething was wrong.")


else:
	print("\nThank you for your interest.")














