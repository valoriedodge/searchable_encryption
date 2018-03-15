text = open("found.txt", "rb")
values = text.readlines()
current = 0
bad = []
with open("new_bad_pcap.txt", "wt") as writeFile:
	for i in range(0, len(values)-1):
	  f =values[i].split(" ")
	  num=int(f[0])
	  
	  # print(current)
	  # print((f[0]-current))
	  if(num>current):
	  	# print(f[0])
	  	current = num
	  	print(current)
	  	if(current==721):
	  		current = 0
	  	#writeFile.write("Change in pcap: ")
	  	#writeFile.write(str(i))
# def read_in_chunks(file): 
#    while True: 
#       data = file.readline() 
#       if not data: break 
#       yield data
# even = 1
# previous = 0
# mygen = read_in_chunks(text)
# for line in mygen:
# 	if (even%2 == 0):
# 		f =line.split(" ")
# 		if(f[0]>current):
# 			current = f[0]
# 			print(current)
# 			bad.append(previous)
# 	previous = line
# 	even += 1
# print(bad)