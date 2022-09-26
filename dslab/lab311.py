''' 
	Name: R.Shyam Sundar
	Date: 26/08/2022
	Data Science Lab: Stack using Linked List
'''

class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.head = Node("Head")
		self.size = 0

	def __str__(self):
		nd = head.node.next
		ans = ""
		while True:
			if nd.next == None:
				ans += nd.value
				return ans
			else:
				ans += nd.value
				ans += " "
				val = val.next

	def GetSize(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def peek(self):
		if self.size == 0:
			print("The Stack is empty!")
			return -1
		else:
			return self.head.next.value

	def push(self, value):
		node = Node(value)
		node.next = self.head.next
		self.head.next = node
		self.size += 1

	def pop(self):
		if self.isEmpty():
			print("Stack is empty!")
			return -1
		remove = self.head.next
		self.head.next = self.head.next.next
		self.size -= 1
		return remove.value

if __name__ == "__main__":
	stack = Stack()
	for i in range(11):
		stack.push(i)
	print(f"Stack: {stack}")

	for _ in range(1, 6):
		remove = stack.pop()
		print(f"Pop: {remove}")
	print(f"Stack: {stack}")