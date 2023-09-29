import time
t = time.strftime("%H:%M:%S")
name = input("Enter your name:")
hour=int(input("\nEnter hour:"))

if(hour>=0 and hour<12):
	print("good morning ",name, "!!")
elif(hour>=12 and hour<17):
	print("good afternoon",name, "!!")
elif(hour>=17 and hour<0):
	print("good night",name, "!!")
#else:
	#print("Invalid entry!!")