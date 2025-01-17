#module to accept 2 numbers from user
while True:
	try:
		num1 = float(input("Enter 1st number: "))
		num2 = float(input("Enter 2nd number: "))
		break
	except ValueError:
		print("Kindly enter numbers only!")

#module to perform mathematical operation
while True:
	print("""Choose the mathematical operation number from the below 4 choices:
		1. Addition (+)
		2. Subtraction (-)
		3. Multiplication (*)
		4. Division (/)""")
	
	try:
		operationID = int(input("Enter the operation number (1-4): "))
		if operationID in (1,2,3,4):
			break
		else:
			print("Invalid choice! Please re-renter the operation number (1-4).")
	except ValueError:
		print ("Kindly enter a numerical value from 1 to 4!")	