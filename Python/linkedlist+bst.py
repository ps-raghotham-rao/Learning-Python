# class Node:
# 	def __init__(self,key):
# 		self.left = None
# 		self.right = None
# 		self.value = key

# # A function to insert a new node with the given key value
# def insert(root,node):
# 	if root is None:
# 		root=node
# 	else:
# 		if root.value<node.value:
# 			if root.right is None:
# 				root.right=node
# 			else:
# 				insert(root.right,node)
# 		else:
# 			if root.left is None:
# 				root.left = node
# 			else:
# 				insert(root.left,node)

# # A function for inorder tree traversal
# def inorder(root):
# 	if root:
# 		inorder(root.left)
# 		print(root.value)
# 		inorder(root.right)




# root= Node(3)
# insert(root,Node(5))
# insert(root,Node(2))
# insert(root,Node(4))
# insert(root,Node(11))
# inorder(root)

def trav(f):
    while f != None:
        print(f.data)
        f=f.next

class Node:
    def __init__(self,data):
        self.next=None
        self.data = data

f=c=Node(1)
while True:
    data=input("Enter data ")
    if data == "-1":
        break
    c.next=Node(data)
    c=c.next
trav(f)