Menu=[[{"0 FoodItems":"Price in Rs."}],
	   {"1 veg.pulao":100},
	   {"2 plain rice":80},
	   {"3 jeera rice":90},
	   {"4 dal fry":100},
	   {"5 chapati":10},
	   {"6 naan":20},
	   {"7 paneer":110}]

for num in range(0,len(Menu)): #printing Menu vertically
	for key,values in Menu.items:
		print(num, key, ":", values)
	Tax = 0.07
	cart={} #empty cart

	def addtocart(key,value):
		item = 0
		while item<=7:
			dish = int(input("Enter the number of dish from the menu"))
			print(dish)
			item +=1
		else:
			print("sorry! you have entered wrong choice.")





