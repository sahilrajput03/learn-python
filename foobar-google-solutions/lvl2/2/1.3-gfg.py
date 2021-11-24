class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
  
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)
 
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Postorder traversal of binary tree is")
printPostorder(root)