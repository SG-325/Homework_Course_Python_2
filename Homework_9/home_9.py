import requests


class Base_1:
	def __init__(self, url):
		self.response = requests.get(url)


	def download(self):
		with open("image.jpeg","wb") as f:
			f.write(self.response.content)




class Base_2:
	def download(self, response):
		with open("image.png","wb") as f:
			f.write(response.content)




class Derived(Base_1, Base_2):
	def __init__(self, url):
		Base_1.__init__(self, url)


	def download(self):
		while True:
			c = input("\nEnter the image format: jpeg or png.\t")
			if c.lower() == "jpeg" or c.lower() == "png":
				break


		if c.lower() == "jpeg":
			Base_1.download(self)
		else:
			Base_2.download(self, self.response)





obj = Derived("http://www.httpbin.org/image/jpeg")
obj.download()
