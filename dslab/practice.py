import numpy as np

def calc_uptri(m1):
	row,cols = m1.shape
	print(rows,cols)
	x = 0
	upper_tri = []
	for i in range(0,rows):
		for j in range(0,cols):
			if j<x:
				pass
			else:
				upper_tri.append(m1[i][j])
				pass
		x = x+1

	print("upper triangular matrix = ",upper_tri)
	pass	

def all_operations(m):
	# Trace of matrix
	print("Trace of a matrix")
	print(m.T)
	pass

rows = int(input("Enter the number of rows in the matrix:  "))
columns = int(input("Enter the number of columns in the matrix:  "))

print("Enter each element in the matrix in new line:  ")
l = []
for i in range(0,rows*columns):
	x = int(input())
	l.append(x)


print("The list:  ",l)
m = np.array(l).reshape(rows,columns)

print("matrix = ",m)

calc_uptri(m)
all_operations(m)

