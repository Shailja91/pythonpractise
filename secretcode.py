import random
import string

str=input("Enter the string")
coding=input(" enter 0 for coding,1 for decoding")
if(coding == "0"):
	coding=True
elif(coding=="1"):
	coding=False
if(coding == True):
	if len(str)>=3:

		a=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)
		str=a + str[::-1] + a
		print(str)
	else:
		print(str[::-1])
else:
	if len(str)>=3:
		str=str[::-1]
		str=str[3:-3]
		print(str)