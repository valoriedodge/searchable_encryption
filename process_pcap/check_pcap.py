##Check for only the longest rule in the data set, creating end-to-end rule tokens, first with one length and then all of the smaller tokens with a smaller length

#Split a given string into all of it's n-sized tokens
def tokenizeString(input_string, n):
	arr = []
	length = len(input_string)
	remain = length % n
	for i in range(0, length-remain, n):
		arr.append((input_string[i:i+n]))
	if remain > 0:
		arr.append(input_string[-n:])
 	return arr


# def matchedData(b, data_path, num, rule_tokens):
# 	data = open(data_path, "r")
# 	dataset = data.read()
# 	boo = b
# 	# b = [False] * len(dataset)
# 	for i in range(len(dataset)):
# 		datatoken = dataset[i:i+num]
# 		if (datatoken in rule_tokens):
# 			for j in range(i,i+num):
# 				b[j] = True
# 	return boo

#Given a path to a data file, creates array of all of the n-sized tokens that match IDS rule tokens and an array of all of the tokens that do not.
def matchedData(data_path, num1, num2, rule_tokens):
	data = open(data_path, "r")
	dataset = data.read()
	b = [False] * len(dataset)
	for i in range(len(dataset)):
		datatoken = dataset[i:i+num]
		if datatoken in rule_tokens:
			for j in range(i,i+num):
				b[j] = True
		rejdatatoken = dataset[i:i+rejNum]
		if rejdatatoken in rejectedRules:
			for k in range(i,i+rejNum):
				b[k] = True
	return sum(b)

# Incorparate all of the methods to return effectiveness of rule detection
# tokenSizes = [4,5,6,7,8,9,10,11,12,13]
# testDataSets = ["nytimes.txt", "cnn.txt", "wsj.txt"]
# with open("variable_rule_results2.txt", "wt") as writeFile:
# 	for num in tokenSizes:
# 		rule_results = tokenizeLongestRules("http_rules.txt", num)
# 		rule_tokens = rule_results[0]
# 		rejectedRules = tokenizeRuleset(rule_results[1], 5)
# 		writeFile.write("*******************************************************************\n")
# 		writeFile.write("Token Size %d \n" %num)
# 		writeFile.write("The number of rejected rules: %d \n\n" %len(rejectedRules[1]))
# 		for data in testDataSets:
# 			results = matchedData(data, num, rule_tokens, rejectedRules[0], 5)
# 			writeFile.write(data)
# 			dataFile = open(data, "r")
# 			datastring = dataFile.read()
# 			writeFile.write("\n")
# 			writeFile.write("The number of matched data characters: %d \n" %results)
# 			percent = (100.0 * results)/len(datastring)
# 			writeFile.write("%.2f \n\n" %percent)
firstTokens = [13,15,17]
secondToken = [3,4,5,6,7, 8]
testDataSets = ["nytimes.txt", "cnn.txt", "wsj.txt"]
with open("change_variable_rule_results.txt", "wt") as writeFile:
	for num in firstTokens:
		writeFile.write("*******************************************************************\n")
		writeFile.write("*******************************************************************\n")
		writeFile.write("Token Size %d \n" %num)
		for second in secondToken:
			rule_results = tokenizeLongestRules("http_rules.txt", num)
			rule_tokens = rule_results[0]
			rejectedRules = tokenizeRuleset(rule_results[1], second)
			writeFile.write("*******************************************************************\n")
			writeFile.write("The number of longest rule tokens: %d \n" %len(rule_tokens))
			writeFile.write("The number of rule tokens: %d \n" %len(rejectedRules[0]))
			writeFile.write("Second Token Size %d \n" %second)
			writeFile.write("The number of rejected rules: %d \n\n" %len(rejectedRules[1]))
			for data in testDataSets:
				results = matchedData(data, num, rule_tokens, rejectedRules[0], second)
				writeFile.write(data)
				dataFile = open(data, "r")
				datastring = dataFile.read()
				writeFile.write("\n")
				writeFile.write("The number of matched data characters: %d \n" %results)
				percent = (100.0 * results)/len(datastring)
				writeFile.write("%.2f \n\n" %percent)
