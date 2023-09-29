questions = [["1. Who developed Python Programming Language?",
"a) Wick van Rossum",
"b) Rasmus Lerdorf",
"c) Guido van Rossum",
"d) Niene Stom"], ["2. Which type of Programming does Python support?",
"a) object-oriented programming",
"b) structured programming",
"c) functional programming",
"d) all of the mentioned"], ["3. Is Python case sensitive when dealing with identifiers?",
"a) no",
"b) yes",
"c) machine dependent",
"d) none of the mentioned"],["4. Which of the following is the correct extension of the Python file?",
"a) .python",
"b) .pl",
"c) .py",
"d) .p"],["5. Is Python code compiled or interpreted?",
"a) Python code is both compiled and interpreted",
"b) Python code is neither compiled nor interpreted",
"c) Python code is only compiled",
"d) Python code is only interpreted"], ["6. All keywords in Python are in _________",
"a) Capitalized",
"b) lower case",
"c) UPPER CASE",
"d) None of the mentioned"]]
levels = [1000,2000,4000,8000,16000,32000,50000]
money=0

for i in range (0,len(questions)):
	question=questions[i]
	print(f"{question[0]}")
	print(f"{question[1]}			{question[2]}")
	print(f"{question[3]}			{question[4]}")

	reply = (int(input("Enter your option from 1-4")))

	if(reply==question[-2]):
			print(f"correct answer !! you have won prize of Rs.{levels[i]}")


			if(i==2):
				money=2000
			elif(i==4):
				money=8000
			elif(i==6):
				money=32000
	else:
				print("You lost!! Game Over!!")
				break