text = open("found.txt", "rb")
values = text.readlines()
text2 = open("found.txt", "rb")
i = 0
for line in text2:
	f = values[i].split(" ")
	f2 = line.split(" ")
	num = int(f[0])
	num2 = int(f2[0])
	if(num != num2):
		print(i)
	i+=1



