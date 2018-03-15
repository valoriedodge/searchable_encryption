#Find the total number of rejected rules, not just tokens, for method 1 and 2

#Regular function to get list of all rules as content arrays
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
	print(len(ruleset))
	return ruleset


#Incorparate all of the methods to return effectiveness of rule detection
tokenSizes = [4,5,6,7,8,9,10,11, 12]
with open("total_rejected_rules.txt", "wt") as writeFile:
	for num in tokenSizes:
		rules_set = getContentRulesList("http_rules.txt")
		rules_rejected = 0
		for rule in rules_set:
			for x in rule:
				if(len(x) < num):
					rules_rejected += 1
					break
		writeFile.write("*******************************************************************\n")
		writeFile.write("Token Size %d \n" %num)
		writeFile.write("The number of rejected rules: %d \n\n" %rules_rejected)
		
