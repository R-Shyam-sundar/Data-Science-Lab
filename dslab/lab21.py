'''
	Name: R.Shyam Sundar
	Roll: CS20B1029
	Date: 12/08/2022 
	Data Science Lab - 2
'''

Dict = {}
while 1:
	print("1:Insert\n2:Delete\n3:Search\n4:Exit")
	choice = int(input("Enter your choice:  "))
	
	if choice == 1:
		y = input("Enter the roll number of the student : ")
		lis = []
		x = input("Enter the Name of the student: ")
		lis.append(x)
		x = input("Enter the CGPA of the student: ")
		lis.append(x)
		x = input("Enter the Mobile number of the student: ")
		lis.append(x)
		Dict[y] = lis;
	elif choice == 2:
		print(Dict)
		x = input("Enter the roll number of the student to be deleted : ")
		if x in Dict.keys():
			Dict.pop(x)
			print("Student successfully removed from the data")
		else:
			print("Roll number doesn't exist in records")
	elif choice == 3:
		print(Dict)
		y = input("Enter the roll number of the student : ")
		if y in Dict.keys():
			print(Dict[y])
		else:
			print("Key is not present in the data")
	elif choice == 4:
		print("Thank you!")
		break;
	else:
		print("Enter a valid choice")
	