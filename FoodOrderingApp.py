Menu={"FoodItems":"Price in Rs.",
	  "veg.pulao":100,
	  "plain rice":80,
	  "jeera rice":90,
	  "dal fry":100,
	  "chapati":10,
	  "naan":20,
	  "paneer":110}

for key,value in Menu.items(): #printing Menu vertically
	print(key,"		",":",value)
	Tax = 0.07
	cart={} #empty cart

	def addtocart(key,value):



