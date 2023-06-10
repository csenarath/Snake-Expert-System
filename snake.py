from experta import *
from art import print_snake

snake_list = []
snake_attributes = []
attributes_map = {}
snake_desc_map = {}
attributes_map2 = {}

def preprocess():


	global snake_list,snake_attributes,attributes_map,snake_desc_map
	
	snake_list_file=open("snakes.txt")
	snake_list =snake_list_file.read().split("\n")
	snake_list_file.close()

	for snake in snake_list:

		snake_attributes_file = open("Snake attributes/" + snake + ".txt")
		snake_attributes_data = snake_attributes_file.read()
		s_list = snake_attributes_data.split("\n")
		snake_attributes.append(s_list)
		attributes_map[str(s_list)] = snake
		data={}
		for line in s_list:
			key, value = map(str.strip, line.split(':'))
			data[key] = value
		attributes_map2[snake]=data
		snake_attributes_file.close()

		

		snake_desc_file = open("Snake descriptions/" + snake + ".txt")
		snake_desc_data = snake_desc_file.read()
		snake_desc_map[snake] = snake_desc_data
		snake_desc_file.close()
	

def identify_disease(*arguments):
	attributes_list = []
	for attributes in arguments:
		attributes_list.append(attributes)
	# Handle key error
	return attributes_map[str(attributes_list)]

def get_details(snake):
	return snake_desc_map[snake]


def if_not_matched(snake):
		id_snake = snake
		snake_details = get_details(id_snake)
		print("")
		print("The most probable snake is %s\n" %(id_snake))
		print("Description of the snake is given below :\n")
		print(snake_details+"\n")
		print("------------------------------------------------: \n")

# @my_decorator is just a way of saying just_some_function = my_decorator(just_some_function)
#def identify_disease(headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever,sunken_eyes):
class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("")
		print_snake()
		print("For that you'll have to answer a few questions about suspected snake")
		print("")
		yield Fact(action="find_snake")

#quctions
	@Rule(Fact(action='find_snake'), NOT(Fact(tail_shape=W())),salience = 1)
	def attribute_0(self):
		self.declare(Fact(tail_shape= {
				"a": "Flattened", 
				"b": "Paddle shaped",
				"c": "Round",
				"d": "Tapering to a point",
				"e": "Blunt"
				 }.get(input("What is the tail shape of the snake?\n a) Flattened\n b) Paddle shaped\n c) Round\n d) Tapering to a point\n e) Blunt\n"), "Invalid input")))

	@Rule(Fact(action='find_snake'), NOT(Fact(near_sea=W())),salience = 0)
	def attribute_01(self):
		self.declare(Fact(near_sea= {
				"y": "yes", 
				"n": "no",
				 }.get(input("Did your snake found near Sea ?\n y) Yes\n n) No\n"), "Invalid input")))
	
	@Rule(Fact(action='find_snake'), NOT(Fact(shape_ventral_scales=W())),salience = 0)
	def attribute_03(self):
		self.declare(Fact(shape_ventral_scales= {
				"a": "Not extended to full body width", 
				"b": "Extended to full body width",
				 }.get(input("What is the shape of ventral scales in back (near tail) on snake ?\n a) Not extended to full body width\n b) Extended to full body width\n"),
	   				 "Invalid input")))
	
	@Rule(Fact(action='find_snake'), NOT(Fact(head_shape=W())),salience = -1)
	def attribute_04(self):
		self.declare(Fact(head_shape= {
				"a": "Triangular shape head", 
				"b": "Neck well defined",
				"c": "Oval shape head",
				"d": "Neck not well defined",
				 }.get(input("What is the shape of head / neck on the snake?\n a) Triangular shape head\n b) Neck well defined\n c) Oval shape head\n d) Neck not well defined\n"), "Invalid input")))


	@Rule(Fact(action='find_snake'), NOT(Fact(expandable_hood=W())),salience = -2)
	def attribute_05(self):
		self.declare(Fact(expandable_hood= {
				"y": "yes", 
				"n": "no",
				 }.get(input("is it have Expandable hood?\n y) Yes\n n) No\n "), "Invalid input")))

	@Rule(Fact(action='find_snake'), NOT(Fact(hexagonal_vertebral_scales=W())),salience = -3)
	def attribute_06(self):
		self.declare(Fact(hexagonal_vertebral_scales= {
				"y": "yes", 
				"n": "no",
				 }.get(input("is it have hexagonal vertebral scales?\n y) Yes\n n) No\n"), "Invalid input")))
		
	@Rule(Fact(action='find_snake'), NOT(Fact(loreal_pit_present=W())),salience = -2)
	def attribute_07(self):
		self.declare(Fact(loreal_pit_present= {
				"y": "yes", 
				"n": "no",
				 }.get(input("is it have Loreal pit present?\n y) Yes\n n) No\n"), "Invalid input")))
		
	@Rule(Fact(action='find_snake'), NOT(Fact(color_scales_size=W())),salience = -3)
	def attribute_08(self):
		self.declare(Fact(color_scales_size= {
				"b": "Brown and Large Scales", 
				"g": "Green and Small Scales",
				 }.get(input("is it have ?\n b) Brown and Large Scales\n g) Green and Small Scales\n"), "Invalid input")))

	@Rule(Fact(action='find_snake'), NOT(Fact(head_scales_and_long_body=W())),salience = -3)
	def attribute_09(self):
		self.declare(Fact(head_scales_and_long_body= {
				"y": "yes", 
				"n": "no",
				 }.get(input("is it have large scales on head and longated body ?\n y) Yes\n n) No\n"), "Invalid input")))

	@Rule(Fact(action='find_snake'), NOT(Fact(cross_on_head=W())),salience = -2)
	def attribute_10(self):
		self.declare(Fact(cross_on_head= {
				"y": "yes", 
				"n": "no",
				 }.get(input("is it have cross mark on head ?\n y) Yes\n n) No\n"), "Invalid input")))





#sea Snakes
	@Rule(Fact(action='find_snake'),Fact(tail_shape="Flattened"),Fact(near_sea="yes"))
	def snake_0(self):
		self.declare(Fact(snake="Sea snakes"))

	@Rule(Fact(action='find_snake'),Fact(tail_shape="Paddle shaped"),Fact(near_sea="yes"))
	def snake_1(self):
		self.declare(Fact(snake="Sea snakes"))

#not Sea Sanke
	@Rule(Fact(action='find_snake'),OR(Fact(tail_shape="Round"),Fact(tail_shape="Tapering to a point"),Fact(tail_shape="Blunt")))
	def snake_3(self):
		self.declare(Fact(not_sea_snake="yes"))

#Non venomous snakes
	@Rule(Fact(action='find_snake'),Fact(not_sea_snake="yes"),Fact(shape_ventral_scales="Not extended to full body width"))
	def snake_4(self):
		self.declare(Fact(snake="Non venomous snakes"))
	



#Snake type 1/2
	@Rule(Fact(action='find_snake'),Fact(not_sea_snake="yes"),OR(Fact(head_shape="Oval shape head"),Fact(head_shape="Neck not well defined")))
	def snake_6(self):
		self.declare(Fact(type_snake="type1"))
	@Rule(Fact(action='find_snake'),Fact(not_sea_snake="yes"),OR(Fact(head_shape="Triangular shape head"),Fact(head_shape="Neck well defined")))
	def snake_5(self):
		self.declare(Fact(type_snake="type2"))



#Cobra
	@Rule(Fact(action='find_snake'),Fact(type_snake="type1"),Fact(expandable_hood="yes"))
	def snake_61(self):
		self.declare(Fact(snake="Cobra"))

	@Rule(Fact(action='find_snake'),Fact(type_snake="type1"),Fact(expandable_hood="no"))
	def snake_62(self):
		self.declare(Fact(type_snake="type11"))
	

#Kraits
	@Rule(Fact(action='find_snake'),Fact(type_snake="type11"),Fact(hexagonal_vertebral_scales="yes"))
	def snake_621(self):
		self.declare(Fact(snake="Kraits"))

#Non venomous snakes
	@Rule(Fact(action='find_snake'),Fact(type_snake="type11"),Fact(hexagonal_vertebral_scales="no"))
	def snake_622(self):
		self.declare(Fact(snake="Non venomous snakes"))

#Snake type 21/22
	@Rule(Fact(action='find_snake'),Fact(type_snake="type2"),Fact(loreal_pit_present="yes"))
	def snake_51(self):
		self.declare(Fact(type_snake="type21"))

	@Rule(Fact(action='find_snake'),Fact(type_snake="type2"),Fact(loreal_pit_present="no"))
	def snake_52(self):
		self.declare(Fact(type_snake="type22"))



#Green pit viper
	@Rule(Fact(action='find_snake'),Fact(type_snake="type21"),Fact(color_scales_size="Green and Small Scales"))
	def snake_511(self):
		self.declare(Fact(snake="Green pit viper"))

#Hump nosed viper
	@Rule(Fact(action='find_snake'),Fact(type_snake="type21"),Fact(color_scales_size="Brown and Large Scales"))
	def snake_512(self):
		self.declare(Fact(snake="Hump nosed viper"))

#cat snake
	@Rule(Fact(action='find_snake'),Fact(type_snake="type22"),Fact(head_scales_and_long_body="yes"))
	def snake_512(self):
		self.declare(Fact(snake="Cat snakes"))

#Saw scale viper
	@Rule(Fact(action='find_snake'),Fact(type_snake="type22"),Fact(head_scales_and_long_body="no"),Fact(cross_on_head="yes"))
	def snake_513(self):
		self.declare(Fact(snake="Saw scale viper"))

#Russell's viper
	@Rule(Fact(action='find_snake'),Fact(type_snake="type22"),Fact(head_scales_and_long_body="no"),Fact(cross_on_head="no"))
	def snake_514(self):
		self.declare(Fact(snake="Russell's viper"))

	

	

	


#matching
	@Rule(Fact(action='find_snake'),Fact(snake=MATCH.snake),salience = -998)
	def snake(self, snake):
		print("")
		id_snake = snake
		snake_details = get_details(id_snake)

		print("")
		print("The most probable snake  is %s\n" %(id_snake))
		print("Description of the snake is given below :\n")
		print(snake_details+"\n")
		print("------------------------------------------------: \n")

	@Rule(Fact(action='find_snake'),
		  Fact(tail_shape=MATCH.tail_shape),
		  Fact(near_sea=MATCH.near_sea),
		  Fact(shape_ventral_scales=MATCH.shape_ventral_scales),
		  Fact(head_shape=MATCH.head_shape),
		  Fact(expandable_hood=MATCH.expandable_hood),
		  Fact(hexagonal_vertebral_scales=MATCH.hexagonal_vertebral_scales),
		  Fact(loreal_pit_present=MATCH.loreal_pit_present),
		  Fact(color_scales_size=MATCH.color_scales_size),
		  Fact(head_scales_and_long_body=MATCH.head_scales_and_long_body),
		  Fact(cross_on_head=MATCH.cross_on_head),NOT(Fact(snake=MATCH.snake)),salience = -999)

	def not_matched(self,tail_shape, near_sea, shape_ventral_scales, head_shape, expandable_hood, hexagonal_vertebral_scales, loreal_pit_present, color_scales_size,
		 			head_scales_and_long_body ,cross_on_head):
		print("\nDid not find any Snake that matches your explanation")
		lis = [tail_shape, near_sea, shape_ventral_scales, head_shape, expandable_hood, hexagonal_vertebral_scales, loreal_pit_present, color_scales_size,
	 			head_scales_and_long_body ,cross_on_head]
		dict= {'tail_shape':tail_shape, "near_sea":near_sea, 
	 			"shape_ventral_scales":shape_ventral_scales, "head_shape":head_shape,
	 			 "expandable_hood":expandable_hood, "hexagonal_vertebral_scales":hexagonal_vertebral_scales,
				 "loreal_pit_present":loreal_pit_present, "color_scales_size":color_scales_size,
	 			"head_scales_and_long_body" :head_scales_and_long_body ,"cross_on_head":cross_on_head}
		max_count = 0
		max_disease = ""
		for key,val in attributes_map2.items():
			snake_=key
			count = 0
			temp_dic = val
			for key,val in dict.items():
				if(temp_dic[key] == val):
					count = count + 1

			if count > max_count:
				max_count = count
				max_disease = snake_
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	#print({"a": "Round", "b": "Flat", "c": "Normal"}.get(input("What is the tail shape of the snake?\n a) Round\n b) Flat\n c) Normal\n"), "Invalid input"))
	while(1):
		engine.reset()  # Prepare the engine for the execution.
		engine.run()  # Run it!
		print(engine.facts)
		print("_________________________________________________")
		print("")
		print("Would you like to check other Snake?")
		if input() == "n":
			exit()
