class Node:
    def __init__(self, index):
        self.left = None
        self.right = None
        self.index = index

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

height = 2
root = build_tree(height)
print('build pefect tree of height', height) 

print(root.left.index)
# print(root.right)
# print(root.left.left)
# print(root.left.right)
# print(root.right.left)
# print(root.right.right)
