name = input("Enter your name: ")

while True:
	try:
		age = int(input("Enter your age in years in integer format: "))
		break
	except ValueError:
		print("Kindly enter whole numbers only!")		

while True:
	try:
		height = int(input("Enter your height in centimeters in integer format: "))
		break
	except ValueError:
		print("Kindly enter whole numbers only!")

newAge = age + 10
heightMeters = height/100
print(f" My name is {name}. I will be {newAge} years old in 10 years and {heightMeters} meters tall.")




