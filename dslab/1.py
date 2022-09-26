'''
Name : R.Shyam Sundar
Roll : CS20B1029
Date : 05/08/22

Data Science Lab1: Q1 : Sort the list using insertion sort
'''

n = int(input("Enter the number of elements in the list :  "))
lis = []

print("Enter the elements in the list : ")

for i in range(0,n):
	inp = int(input())
	lis.append(inp)

print("The list is : ",lis)


for i in range(1,n):
	val = lis[i]

	j = i-1
	while j >= 0 and lis[j] > val:
		lis[j+1] = lis[j]
		lis[j] = val
		j = j-1

print("The sorted list is: ",lis)
