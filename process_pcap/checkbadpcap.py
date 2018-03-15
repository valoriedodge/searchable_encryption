#Check Pcap for all of the content strings to see if there is a rule match

#Create an array of all of the rule arrays of content strings
def get_content_rules_list(rule_path):
	ruleset = []
	rule_file = open(rule_path, "r") 
	for line in rule_file: 
		 splitline = line.split("; ")
		 #Create an array for all of the content strings in the rule
		 rule_contents = []
		 for word in splitline:
		 	if word.startswith("content"):
		 		rule = word[9:-1]
		 		#appednd each content string to the rule array
		 		rule_contents.append(rule)
		 # Append the rule array to the ruleset array
		 ruleset.append(rule_contents)
	return ruleset

#create a rule object of each rule array of content strings
# This object should have an array of content string arrays- containing all of the string tokens
# Object should have array of tokens still to find for each content string array
def make_rule_obj(rule):
	rule_object = {}
	#create array to hold the content arrays with big token size
	rule_object["big_tokens"] = []
	#create array to hold the content arrays with big small size
	rule_object["small_tokens"] = []
	#create array to track which indexes haven't been seen for each content array for big tokens
	rule_object["big_to_find"] = []
	#create array to track which indexes haven't been seen for each content array for small tokens
	rule_object["small_to_find"] = []
	#For each content string in the rule determine what size it will be tokenized 
	for content in rule:
		tokens = []
		find_idx = []
		if(len(content) >= n1):
			#tokenized the content and add it to the content array
			tokens = tokenize_string(content, n1)
			#add token array to the objects array of content arrays
			rule_object["big_tokens"].append(tokens)
			for i in range(0, len(tokens)):
				find_idx.append(i)
			rule_object["big_to_find"].append(find_idx)
		else if(len(content) >= n2):
			tokens = tokenize_string(content, n2)
			rule_object["small_tokens"].append(tokens)
			for i in range(0, len(tokens)):
				find_idx.append(i)
			rule_object["small_to_find"].append(find_idx)
	return rule_object

#Make a list of all of the rule objects
def make_rule_obj_list(ruleset):
	object_rule_list = []
	for rule in ruleset:
		object_rule_list.append(makeRuleObj(rule))

def add_token_to_set(token_dict, token, index):
	if token in token_dict:
		if index not in token_dict[token]:
			token_dict[token].append(index)
	else:
		token_dict[token]= [index]


def find_index_found_token(ruleset, token):
	index_array = token_dict[token]
	for idx in index_array:
		rule_object = ruleset[idx]
		if len(token) == n1:
			found = [(i, arr.index(token))
 			for i, arr in enumerate(rule_object["big_tokens"])
 				if token in arr]
 			for tup in found:
 				i1, i2 = tup
 				if i2 in rule_objects["big_to_find"][i1]:
 					rule_objects["big_to_find"][i1].remove(i2)
 		if len(token) == n2:
			found = [(i, arr.index(token))
 			for i, arr in enumerate(rule_object["small_tokens"])
 				if token in arr]
 		







#Split a given string into all of it's n-sized tokens
def tokenize_string(input_string, n):
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
