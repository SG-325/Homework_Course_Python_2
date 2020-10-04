from f_1 import func

sample_data = {'1':['a','b'], '2':['c','d'], '3':['e','f']}

print("\nDictionary:",sample_data)
print("\nAll letter combinations.")

for i in func(sample_data):
	print("\t", i)
