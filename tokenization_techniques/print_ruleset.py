firstToken = 11
secondToken = 3

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


#Split all of the content rules into each of their n-sized tokens- also track which rules are rejected on account of being smaller than n
def tokenizeRuleset(rule_set, num, rule_array):
	rejectedRules = []
	rule_token_arr_list = rule_array
	rule_tokens = set()
	for rule in rule_set:
		if (len(rule) < num):
			rejectedRules.append(rule)
		else:
			rule_substrings = tokenizeString(rule, num)
			rule_token_arr_list.append(rule_substrings)
			rule_tokens.add(rule_substrings[0])
	return [rule_tokens, rejectedRules, rule_token_arr_list]

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

def tokenizeLongestRules(rule_path, num, rule_array):
	ruleset = getContentRulesList(rule_path)
	rule_token_arr_list = rule_array
	rejectedRules = set()
	rule_tokens = set()
	for rule in ruleset:
		longest = rule[0]
		for x in rule:
			if len(x) > len(longest):
				longest = x
		if (len(longest) < num):
			rejectedRules.add(longest)
		else:
			rule_substrings = tokenizeString(longest, num)
			rule_token_arr_list.append(rule_substrings)
			rule_tokens.add(rule_substrings[0])
			# rule_tokens.update(rule_substrings)
	return [rule_tokens, rejectedRules]


with open("ruleset.txt", "wt") as writeFile:
	rule_results = tokenizeLongestRules("http_rules.txt", firstToken)
	rule_tokens = rule_results[0]
	rejectedRules = tokenizeRuleset(rule_results[1], secondToken)
	for rule in rule_tokens:
		writeFile.write(rule)
		writeFile.write("\n")
	second_rule_tokens = rejectedRules[0]
	for rule in second_rule_tokens:
		writeFile.write(rule + "\n")

	
