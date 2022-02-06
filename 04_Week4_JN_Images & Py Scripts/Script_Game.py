
def NameGame():
	newname = ""
	while newname != "quit":
		newname = input("What's your name? ")
		if newname != "quit":
			print("Hi, {}! Give me another name".format(newname))
		else:
			print("Goodbye")	

