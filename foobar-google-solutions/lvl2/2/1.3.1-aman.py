height = 3

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

countForTree = 0
def build_tree(h):
    global countForTree
    countForTree = countForTree + 1
    node = Node(countForTree)
    if h == 1:
        return node
    node.left = build_tree(h-1)
    node.right = build_tree(h-1)
    return node

root = build_tree(height)
print('build pefect tree of height', height) 

count = 0
  
# A function to do postorder tree traversal
def visitInPostOrder(root):
    if root:
        global count
        visitInPostOrder(root.left)
        root.left = count
        count = count + 1
        visitInPostOrder(root.right)
        root.right = count
        count = count + 1
        root.data = count
        count = count + 1
        
        
        # print(root.index)
        # global count
        # count = count + 1
        # root.data = count
        print('data', root.data)
 
visitInPostOrder(root)
