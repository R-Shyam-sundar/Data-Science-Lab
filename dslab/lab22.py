'''
	Name: R.Shyam Sundar
	Roll: CS20B1029
	Date: 12/08/2022 
	Data Science Lab - 2
'''

Dict = {}
index = 0;
while 1:
	print("-----------------------------------------------------------------------------------")
	print("1:Create Empty set\n2:Insert\n3:Delete\n4:Search\n5:Print\n6:Union\n7:Interection\n8:Set Difference\n9:Symmetric Difference\n10:Exit\n\n")
	print("-----------------------------------------------------------------------------------")
	
	choice = int(input("Enter your choice: "))
	print(choice)
	if choice == 1:
		Dict[index] = set()
		print("Empty set created with index = ",index)
		index = index+1;
		
	elif choice == 2:
		print(Dict)
		if len(Dict) == 0:
			print("The dictionary is empty")
			continue
		x = int(input("Enter the index of the set : "))
		if x in Dict.keys():
			y = input("Enter the value to be added to set : ")
			Dict[x].add(y)
			print("Value successfully added")
		else:
			print("Index doesn't exist")
		pass
	elif choice == 3:
		x = int(input("1:Delete a set\n2:Delete an element in the set"))
		if x == 1:
			y = int(input("Enter the index of the set"))
			if y in Dict.keys():
				Dict.pop(y)
			else:
				print("Index doesn't exist")
			pass
		elif x == 2:
			z = int(input("Enter the index of the set:  "))
			if z in Dict.keys():
				y = input("Enter the value to be deleted:  ")
				Dict[z].remove(y)
			else:
				print("Index doesn't exist")
			pass
		else:
			print("Enter a valid choice")
		pass
	elif choice == 4:
		y = int(input("Enter the index of the set : "))
		if y in Dict.keys():
			print(Dict[y])
		else:
			print("Index doesn't exist")
		pass
	elif choice == 5:
		print(Dict)
		pass
	elif choice == 6:
		x1 = int(input("Enter the index of the first set : "))
		x2 = int(input("Enter the index of the second set : "))
		x3 = set()
		x3 = Dict[x1].union(Dict[x2])
		print(x3)
		pass
	elif choice == 7:
		x1 = int(input("Enter the index of the first set : "))
		x2 = int(input("Enter the index of the second set : "))
		x3 = set()
		x3 = Dict[x1].intersection(Dict[x2])
		print(x3)
		pass
	elif choice == 8:
		x1 = int(input("Enter the index of the first set : "))
		x2 = int(input("Enter the index of the second set : "))
		x3 = set()
		x3 = Dict[x1].difference(Dict[x2])
		print(x3)
		pass
	elif choice == 9:
		x1 = int(input("Enter the index of the first set : "))
		x2 = int(input("Enter the index of the second set : "))
		x3 = set()
		x3 = Dict[x1].difference(Dict[x2])
		x4 = set()
		x4 = Dict[x2].difference(Dict[x1])
		print(x3.union(x4))
		pass
	elif choice == 10:
		print("Thank you!")
		break;
	else:
		print("Enter a valid choice")