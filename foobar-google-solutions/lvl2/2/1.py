class Node:
   def __init__(self, data=None):
    self.data = data
    self.leftNode = None
    self.rightNode = None


# height 2
height = 2
rootValue = 2**height -1
print('My root value is', rootValue, 'for tree of height', height)

rootNode = Node(rootValue)

rootNode.leftNode = Node(1)
rootNode.rightNode = Node(2)