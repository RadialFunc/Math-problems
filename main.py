import requests
import os


for n in range (2016, 2017):
	#parent  = os.getcwd()
	#path = parent+"/AMC12/B/"+str(n)
	#os.makedirs(path)
	for problem in range (9,26):
		img_data = requests.get(f"https://ggim.me/images/AMC-12B-{n}-P{problem}").content
		f= open(f'AMC12/B/{n}/{problem}.png', 'x')
		f = open(f'AMC12/B/{n}/{problem}.png', 'wb')
		f.write(img_data)

