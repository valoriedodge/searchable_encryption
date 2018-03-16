#Parse through IDS rules from given path to return array of all content rules
def getAllContentRules(rule_path):
	ruleset = []
	rule_file = open(rule_path, "r") 
	for line in rule_file: 
		 splitline = line.split("; ")
		 for word in splitline:
		 	if word.startswith("content"):
		 		rule = word[9:-1]
		 		ruleset.append(rule)
	return ruleset

#Parse through IDS rules from given path to create sub-arrays of search terms for each content rule and return array of all content rules
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

#Create a count of all of the different rule lengths
def countRuleLengths(rule_path):
	ruleset = getAllContentRules(rule_path)
	ruleCounts = [0] * 40
	for rule in ruleset:
		while len(ruleCounts) <= len(rule):
		  ruleCounts.append(0)
		ruleCounts[len(rule)] += 1 
	grouped_counts = []
	for x in range(1, len(ruleCounts), 10):
		grouped_counts.append(sum(ruleCounts[x:x+10]))
	    
	return grouped_counts

#Create a count of the longest rule length per rule
def countLongestRuleLengths(rule_path):
	ruleset = getContentRulesList(rule_path)
	ruleCounts = [0] * 40
	for rule in ruleset:
		longest = rule[0]
		for x in rule:
			if len(x) > len(longest):
				longest = x
		while len(ruleCounts) <= len(longest):
		  ruleCounts.append(0)
		ruleCounts[len(longest)] += 1 
	grouped_counts = []
	for x in range(1, len(ruleCounts), 10):
		grouped_counts.append(sum(ruleCounts[x:x+10]))
	    
	return grouped_counts


#Incorparate all of the methods to return effectiveness of rule detection
with open("newrules.txt", "wt") as f:
	rule_counts = countRuleLengths("http_rules.txt")
	longest_rule_counts = countLongestRuleLengths("http_rules.txt")
	for i in range(1, len(rule_counts)):
		f.write("%d rules with length of %d-%d \n" %(rule_counts[i], ((i-1)*10)+1, i*10 ))
	for i in range(1, len(longest_rule_counts)):
		f.write("%d rules with longest length of %d-%d \n" %(longest_rule_counts[i], ((i-1)*10)+1, i*10 ))
