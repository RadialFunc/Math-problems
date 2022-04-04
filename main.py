import requests
import os


for n in range (2002, 2022):
	parent  = os.getcwd()
	path = parent+"/AMC10/A/"+str(n)
	os.makedirs(path)
	for problem in range (1,26):
		img_data = requests.get(f"https://ggim.me/images/AMC-10A-{n}-P{problem}").content
		f= open(f'AMC10/A/{n}/{problem}.png', 'x')
		f = open(f'AMC10/A/{n}/{problem}.png', 'wb')
		f.write(img_data)
print('Hi rohan, this is a test and i dont know what im doing!');
