class Ruleset:
	def __init__(self, number):
        self.number = number
        self.rules = []
          

    def add_rule(self, rule):
        self.rules.append[rule]
    
    def add_second_tokens(self, tokens):
        self.second_tokens = tokens
        for i in range(0,len(second_tokens)):
    		self.second_to_find.append(i)

    def check_if_found():
    	if (len(self.first_to_find) ==0 and len(self.second_to_find) ==0):
    		return True
    	else:
    		return False