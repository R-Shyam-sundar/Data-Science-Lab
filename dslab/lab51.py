'''
	Name: R.Shyam Sundar
	Roll: CS20B1029
	Date: 13-09-2022
	Data Science lab 5: Numpy arrays 
'''

import numpy
import random

def add_matrix(m1,m2):
	print(numpy.add(m1,m2))
	pass

def sub_matrix(m1,m2):
	print(numpy.subtract(m1,m2))
	pass

def scalar_mul_matrix(m1,m2):
	print(numpy.dot(m1,m2))
	pass

def Elementwise_mul_matrix(m1,m2):
	print(numpy.multiply(m1,m2))
	pass

def transpose_matrix(m1,m2):
	print("The transpose of matrix1:  ")
	print(m1.T)
	print("The transpose of matrix2:  ")
	print(m2.T)
	pass

def mul_matrix(m1,m2):
	print(numpy.matmul(m1,m2))
	pass

def trace_matrix(m1,m2):
	print("The trace of matrix1:  ")
	print(numpy.trace(m1))
	print("The trace of matrix2:  ")
	print(numpy.trace(m2))
	pass

def linear_equations(m1,m2):
	b = numpy.array([1,2])
	print("m1 = ",m1)
	print("b = ",b)
	print("Roots : ",numpy.linalg.solve(m1, b))
	pass

def determinant(m1,m2):
	print("The determinant of matrix1: ")
	print(numpy.linalg.det(m1))
	print("The determinant of matrix2: ")
	print(numpy.linalg.det(m2))
	pass

def inverse(m1,m2):
	print("The inverse of matrix1:  ")
	print(numpy. linalg. inv(m1))
	print("The inverse of matrix2:  ")
	print(numpy. linalg. inv(m2))
	pass

def singular_value_decomposition(m1,m2):
	print("The singular_value_decomposition of matrix1:  ")
	print(numpy.linalg.svd(m1))
	print("The singular_value_decomposition of matrix2:  ")
	print(numpy.linalg.svd(m2))
	pass

def eigen_value(m1,m2):
	print("The eigen_value of matrix1:  ")
	print(numpy.linalg.eig(m1))
	print("The eigen_value of matrix2:  ")
	print(numpy.linalg.eig(m2))
	pass

def search_an_element(m1,m2):
	val = int(input("Enter the value to be searched:  "))
	mat_choice = int(input("Enter the matrix to be searched [1 = matrix1, 2 = matrix2]:   "))
	if mat_choice>2 or mat_choice<1:
		print("Enter a valid choice")
		pass
	else:
		if mat_choice==1:
			print(numpy.where(m1==val))
			pass
		else:
			print(numpy.where(m2==val))
			pass
		pass
	pass

def sum_of_diff_ULTM(m1,m2):
	num_rows,num_cols = m1.shape
	uptri = num_cols
	uptri_list = []
	leave = int(0)
	for r in m1:
		x = leave
		for c in r:
			if x>0:
				x = x - 1
				pass
			else:
				uptri_list.append(c)
				pass

		leave = leave + 1

	print("Elements in upper triangle: ",uptri_list)

	print("Last element = ",m1[num_rows-1][num_cols-1])
	leave = int(0)
	lowertri_list = []
	for i in range(num_rows-1,-1,-1):
		x = leave
		for j in range(0,num_cols):
			if x>0:
				x = x-1
			else:
				lowertri_list.append(m1[i][j])
		leave = leave + 1

	print("Elements in lower triangular matrix:  ",lowertri_list)

	sm1 = 0
	sm2 = 0

	for i in range(0,len(uptri_list)):
		sm1 = sm1 + (int(uptri_list[i]))
	
	for i in range(0,len(lowertri_list)):
		sm2 = sm2 + (int(lowertri_list[i]))

	print("Sum of elements in upper triangular matrix :  ",sm1)
	print("Sum of elements in lower triangular matrix :  ",sm2)
	print("Difference is sum : ",abs(sm1-sm2))
	pass

def printmenu():
	print("1.Matrix Addition")
	print("2.Matrix Subtraction")
	print("3.Scalar Matrix Multiplication")
	print("4.Elementwise Matrix Multiplication")
	print("5.Matrix Multiplication")
	print("6.Matrix Transpose")
	print("7.Trace of a Matrix")
	print("8.Solve System of Linear Equations")
	print("9.Determinant")
	print("10.Inverse")
	print("11.Singular Value Decomposition")
	print("12.Eigen Value")
	print("13.Search an Element")
	print("14.Sum of Difference of Upper and Lower Triangular Matrix")
	print("15.Exit")
	pass


fillmatrix = True
choice = 0;
while True:
	printmenu()	
	if fillmatrix==True:
		rows = int(input("Enter the number of rows in the matrix:  "))
		cols = int(input("Enter the number of columns in the matrix:  "))
		print("Enter the elements of the matrix1 in a single line:  ")
		elem = list(map(int,input().split()))
		m1 = numpy.array(elem).reshape(rows,cols)
		fillmatrix = False
		print("The given matrix:  ")
		print(m1)
		print("Enter the elements of the matrix2 in a single line:  ")
		elem = list(map(int,input().split()))
		m2 = numpy.array(elem).reshape(rows,cols)
		fillmatrix = False
		print("The given matrix:  ")
		print(m2)
		pass

	choice = int(input("Enter your choice:  "))

	if choice==1:
		add_matrix(m1,m2)
		print("---------------------------------------------------")
		pass
	elif choice==2:
		sub_matrix(m1,m2)
		print("---------------------------------------------------")

		pass
	elif choice==3:
		scalar_mul_matrix(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==4:
		Elementwise_mul_matrix(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==5:
		mul_matrix(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==6:
		transpose_matrix(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==7:
		trace_matrix(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==8:
		linear_equations(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==9:
		determinant(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==10:
		inverse(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==11:
		singular_value_decomposition(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==12:
		eigen_value(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==13:
		search_an_element(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==14:
		sum_of_diff_ULTM(m1,m2)
		print("---------------------------------------------------")
	
		pass
	elif choice==15:
		break
		pass
	else:
		print("Enter a valid choice.")
		pass
	pass