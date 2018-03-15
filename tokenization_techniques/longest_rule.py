#Check to see if any rule token matches a given token from the data
def tokenInRules(datatoken, ruleset):
	dataset = set()
	dataset.add(datatoken)
	combine_set = dataset & ruleset
	return len(combine_set) > 0

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
		 		splitword = word.split(":")
		 		rule = splitword[1]
		 		ruleset.append(rule)
	return ruleset

#Split all of the content rules into each of their n-sized tokens- also track which rules are rejected on account of being smaller than n
def tokenizeRuleset(rule_path, num):
	ruleset = getRules(rule_path)
	rejectedRules = []
	rule_tokens = set()
	for rule in ruleset:
		if (len(rule) < num):
			rejectedRules.append(rule)
			continue
		rule_substrings = tokenizeString(rule, num)
		rule_tokens.update(rule_substrings)
	return [rule_tokens, rejectedRules]

#Given a path to a data file, split all of the data into n-sized tokens
def tokenizeData(data_path, num):
	data = open(data_path, "r")
	dataset = []
	for line in data:
		datatokens = tokenizeString(line, num)
		dataset.append(datatokens)
	return dataset

#Given a path to a data file, creates array of all of the n-sized tokens that match IDS rule tokens and an array of all of the tokens that do not.
def matchedData(data_path, num, rule_tokens):
	data = open(data_path, "r")
	dataset = data.read()
	b = [False] * len(dataset)
	for i in range(len(dataset)):
		datatoken = dataset[i:i+num]
		if tokenInRules(datatoken, rule_tokens):
			for j in range(i,i+num):
				b[j] = True
	return sum(b)

def getContentRulesList(rule_path):
	ruleset = []
	rule_file = open(rule_path, "r") 
	for line in rule_file: 
		 splitline = line.split("; ")
		 rule_contents = []
		 for word in splitline:
		 	if word.startswith("content"):
		 		rule = word[9:-1]
		 		rule_contents.append(rule)
		 ruleset.append(rule_contents)
	return ruleset

def tokenizeLongestRules(rule_path, num):
	ruleset = getContentRulesList(rule_path)
	rejectedRules = []
	rule_tokens = set()
	for rule in ruleset:
		longest = rule[0]
		for x in rule:
			if len(x) > len(longest):
				longest = x
		if (len(longest) < num):
			rejectedRules.append(longest)
			continue
		rule_substrings = tokenizeString(longest, num)
		rule_tokens.update(rule_substrings)
	print(rejectedRules)
	return [rule_tokens, rejectedRules]

#Incorparate all of the methods to return effectiveness of rule detection
tokenSizes = [4,5,6,7,8,9]
testDataSets = ["nytimes.txt", "cnn.txt", "wsj.txt"]
with open("longest_rule_results.txt", "wt") as writeFile:
	for num in tokenSizes:
		rule_results = tokenizeLongestRules("http_rules.txt", num)
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
			writeFile.write("The number of matched data characters: %d \n" %results)
			percent = (100.0 * results)/len(datastring)
			writeFile.write("The percent of matched characters: %.2f \n\n" %percent)
