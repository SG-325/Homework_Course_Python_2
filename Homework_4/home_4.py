
class Country:
	def __init__(self, name, continent):
		self.name = name
		self.continent = continent

	def Country_Presentation(self):
		text = F"This product was created on the continent of {self.continent}, in {self.name}."
		return text



class Brand:
	def __init__(self, brand_name, business_date):
		self.brand_name = brand_name
		self.business_date = business_date


	def Brand_Presentation(self):
		text = F"The product brand is {self.brand_name}, and the business start date is {self.business_date}."
		return text


	def same_sort(self, d):
		print(F"{d} is also {self.brand_name}.")

class Season:
	def __init__(self, season_name, average_temperature):
		self.season_name = season_name
		self.average_temperature = average_temperature


	def Season_Presentation(self):
		text = F"The product season is {self.season_name} and the average temperature of use is {self.average_temperature}."
		return text



class Product(Country, Brand, Season):
	def __init__(self, product_name, product_type, product_price, product_quantity, brand_name, business_date, season_name, average_temperature, name, continent):
		self.product_name = product_name
		self.product_type = product_type
		self.product_price = product_price
		self.product_quantity = product_quantity
		Country.__init__(self, name, continent)
		Brand.__init__(self, brand_name, business_date)
		Season.__init__(self, season_name, average_temperature)


	def Product_Presentation(self):
		print(F"\nDescription of our product:\n\tname = {self.product_name}\n\ttype = {self.product_type}\n\tprice = {self.product_price}\n\tquantity = {self.product_quantity}\n")
		print(self.Country_Presentation())
		print(self.Brand_Presentation())
		print(self.Season_Presentation())


	def discount(self):
		self.product_price -= (self.product_price * 5) / 100


	def increase_price(self):
		self.product_price += (self.product_price * 5) / 100

	def increase_quantity(self):
		self.product_quantity += 1



Orange = Product("Orange", "Fruit", 500, 5, "Citrus", "in 314 BC", "Autumn", "15,5-29 °C", "China", "Asia")

Orange.Product_Presentation()


while Orange.product_quantity < 20:
	Orange.increase_quantity()

print("\nIncreased quantity is:", Orange.product_quantity)


if Orange.season_name == "Autumn":
	Orange.discount()
else:
	Orange.increase_price()

print("\nChanged price is:", Orange.product_price)

print("\n")

fruit_dict = {"Mandarin" : "Citrus", "Lemon" : "Citrus", "Raspberry" : "berries"}

for i in fruit_dict:
	if fruit_dict[i] == Orange.brand_name:
		Orange.same_sort(i)


