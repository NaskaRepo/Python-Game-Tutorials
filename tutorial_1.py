#	python -m trace -t tutorial_1.py 

def checkNumber(num, haha):
	if num == "4":
		return "You win!"
	elif num == "69":
		return "Nice!"
	else:
		print(haha + "...  Haha!")
		return "You lose!"

if __name__ == "__main__":
	print("1")
	print("2")
	print("3")

	nextNumber = input("What is the next number?")
	sure = input("Are you sure?")

	message = checkNumber(nextNumber, sure)

	print("-----")
	print(message)

