class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
 
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
 
 
def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        # print(root.data, end=" ")
        print(root.data)
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)
 
def height(node):
    print('node==>', node.data if node != None else 'cool')
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
printLevelOrder(root)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)