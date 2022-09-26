''' 
	Name: R.Shyam Sundar
	Date: 26/08/2022
	Data Science Lab: Queue using Linked List
'''

class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None

class Queue:
	
	def __init__(self):
		self.front = Node
		self.rear = Node

	def isEmpty(self):
		if(self.front == None):
			return True
		else :
			return False
	
	def EnQueue(self, item):
		temp = Node(item)
		
		if self.rear == None:
			self.front = self.rear = temp
			return
		self.rear.next = temp
		self.rear = temp

	def DeQueue(self):
		
		if self.isEmpty():
			return
		temp = self.front
		self.front = temp.next

		if(self.front == None):
			self.rear = None



q = Queue()
for i in range(10):
	q.EnQueue(i)

q.DeQueue()
print("Front: " + str(q.front.data))
print("Rear: " + str(q.rear.data))
	
