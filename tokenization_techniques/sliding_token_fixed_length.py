##Check for each rule token, using sliding token to create rules.

#Split a given string into all of it's n-sized tokens
def tokenizeString(input_string, n):
	arr = []
	length = len(input_string)
 	for i in range(length):
 		if (i+n <= length):
 			arr.append((input_string[i:i+n]))
 	return arr

#Parse through IDS rules from given path to find content rules
def getRules(rule_path):
	ruleset = []
	rule_file = open(rule_path, "r") 
	for line in rule_file: 
		 splitline = line.split("; ")
		 for word in splitline:
		 	if word.startswith("content"):
		 		rule = word[9:-1]
		 		ruleset.append(rule)
	return ruleset

#Split all of the content rules into each of their n-sized tokens- also track which rules are rejected on account of being smaller than n
def tokenizeRuleset(rule_path, num):
	ruleset = getRules(rule_path)
	print(len(ruleset))
	rejectedRules = []
	rule_tokens = set()
	for rule in ruleset:
		if (len(rule) < num):
			rejectedRules.append(rule)
			continue
		rule_substrings = tokenizeString(rule, num)
		rule_tokens.update(rule_substrings)
	# print(rejectedRules)
	return [rule_tokens, rejectedRules]

#Given a path to a data file, creates array of all of the n-sized tokens that match IDS rule tokens and an array of all of the tokens that do not.
def matchedData(data_path, num, rule_tokens):
	data = open(data_path, "r")
	dataset = data.read()
	b = [False] * len(dataset)
	for i in range(len(dataset)):
		datatoken = dataset[i:i+num]
		if (datatoken in rule_tokens):
			for j in range(i,i+num):
				b[j] = True
	return sum(b)

#Incorparate all of the methods to return effectiveness of rule detection
tokenSizes = [4,5,6,7,8, 9, 10,11,12]
testDataSets = ["nytimes.txt", "cnn.txt", "wsj.txt"]
with open("boolresults2.txt", "wt") as writeFile:
	for num in tokenSizes:
		rule_results = tokenizeRuleset("http_rules.txt", num)
		rule_tokens = rule_results[0]
		rejectedRules = rule_results[1]
		writeFile.write("*******************************************************************\n")
		writeFile.write("Token Size %d \n" %num)
		writeFile.write("The number of rejected rules: %d \n\n" %len(rejectedRules))
		for data in testDataSets:
			results = matchedData(data, num, rule_tokens)
			writeFile.write(data)
			dataFile = open(data, "r")
			datastring = dataFile.read()
			writeFile.write("\n")
			writeFile.write("The number data characters: %d \n" %len(datastring))
			writeFile.write("The number of matched data characters: %d \n" %results)
			percent = (100.0 * results)/len(datastring)
			writeFile.write("%.2f \n\n" %percent)
