import json
import threading
import requests


def function(l):
	for i in l:

		p = i["name"]
		print(p)

		with open(f"{p}.jpeg","wb") as f:
			f.write(requests.get(i["url"]).content)


if __name__ == "__main__":

	with open("image_url.json","r") as f:
		dict_ = json.load(f)

	
	thread_list = []
	b = []
	j = 0

	for i in range(5):
		a = []
		a.append(dict_["items"][j])
		a.append(dict_["items"][j+1])
		b.append(a)
		j += 2


	for i in b:	
		x = threading.Thread(target=function, args = (i, ))
		thread_list.append(x)
		x.start()
