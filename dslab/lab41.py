'''
Name : R.Shyam Sundar
Roll : CS20B1029
Date : 05/08/22

Data Science Lab4: Q1 : Write a python program to handle books in a library management system.
 		The information available in a book are book ISSN, book title, price, edition, year, and author name.
 		The library management system should support the following menus,
Write
Read
Search
Exit
		The write option takes ‘n’ book information from the user and writes it into a file. The read option reads all the information stored in a file. The search option allows the search of books based on the book title (assume there are no duplicates).
'''

import pickle
import os

def printMenu():
	print("1: Write")
	print("2: Read")
	print("3: Search")
	print("4: Exit")
	return

def write_to_file():

	if os.stat("data.txt").st_size == 0:
		file1 = open("data.txt","a")
		file1.write("Start\n")

	n = int(input("Enter the number of books to be added :  "))
	for i in range(n):
		file1 = open("data.txt","a")
		issn = input("Enter the ISSN of the book:  ")
		file1.write(issn)
		file1.write("\n")
		title = input("Enter the title of the book:  ")
		file1.write(title)
		file1.write("\n")
		
		price = input("Enter the price of the book:  ")
		file1.write(price)
		file1.write("\n")
		
		edition = input("Enter the edition of the book:  ")
		file1.write(edition)
		file1.write("\n")
		
		year = input("Enter the year of publication:  ")
		file1.write(year)
		file1.write("\n")
		
		author_name = input("Enter the author name:  ")
		file1.write(author_name)
		file1.write("\n")
	return

def read_from_file():
	lines = tuple(open('data.txt', 'r'))
	for i in range(len(lines)):
		if i%6==1:
			print("---------------------------------------")
		temp = lines[i]
		temp = temp[:-1]
		print(temp)
		if(i%6 == 0):
			print("---------------------------------------")
	return

def search_in_file():
	lines = tuple(open('data.txt', 'r'))
	title = input("Enter the name of the book:  ")
	for i in range(len(lines)):
		if i%6==2:
			# print(lines[i])
			temp = lines[i]
			temp = temp[:-1]
			if temp==title:
				print("Book Found!")
				print("Book ISSN: ",lines[i-1])
				print("Book Title:  ",lines[i])
				print("Book Price:  ",lines[i+1])
				print("Book edition:  ",lines[i+2])
				print("Book year:  ",lines[i+3])
				print("Book author:  ",lines[i+4])
				break
	return

if __name__=="__main__":
	choice = 0
	while True:
		choice = int(input("Enter your choice:  ")) 
		if choice==1:
			write_to_file()
		elif choice==2:
			read_from_file()
		elif choice==3:
			search_in_file()
		elif choice==4:
			print("Thank you!")
			break
