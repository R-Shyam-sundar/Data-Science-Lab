'''
Name : R.Shyam Sundar
Roll : CS20B1029
Date : 05/08/22

Data Science Lab 1: Q2: Write a python program to find the element using binary search
'''

n = int(input("Enter the number of elements in the list :  "))

lis = []
print("Enter the elements in the list:  ");
for i in range(0,n):
	inp = int(input())
	lis.append(inp)

print(lis)
lis.sort()
print(lis)

x = int(input("Enter the number of element that has to be find: "))

left = 0
right = n-1
index = -1
while left<=right:
	mid = int(left + int((right - left)/2))
	
	if lis[mid] == x:
		index = mid
		break
	elif lis[left] == x:
		index = left
		break
	elif lis[right] == x:	
		index = right
		break
	elif left == right-1:
		break
	elif lis[mid] < x:
		left = mid
	else:
		right = mid

if index == -1:
	print("Element not found!")
else:
	print("Element found at index : ")
	print(index)

