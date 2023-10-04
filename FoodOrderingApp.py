Menu=[{"FoodItems":"Price in Rs."},{"veg.pulao": 100},{"plain rice": 80},{"jeera rice": 90},{"dal fry": 100},{"chapati": 10},{"naan": 20},{"paneer": 110}]

orderedfood=[]
print("-------Menu-------")
for i, item in enumerate(Menu, start=0):
	dishname = list(item.keys())[0]
	print(i, " ",dishname,"",item[dishname])

orderedfood.append(input("\n What dish do you want."))
print("you've ordered:",list(Menu[int(orderedfood[0])].keys()),"of rs.",list(Menu[int(orderedfood[0])].values()))
orderedf1 = Menu[int(orderedfood[0])]