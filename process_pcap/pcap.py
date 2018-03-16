text = open("found.txt", "rb")
values = text.readlines()
current = 0
bad = []

with open("new_bad_pcap.txt", "wt") as writeFile:
	for i in range(0, len(values)-1):
	  f =values[i].split(" ")
	  num=int(f[0])
	  if(num>current):
	  	current = num
	  	print(current)
	  	if(current==721):
	  		current = 0
