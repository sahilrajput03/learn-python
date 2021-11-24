class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def build_tree(h):
    node = Node(0)
    if h == 1:
        return node
    node.left = build_tree(h-1)
    node.right = build_tree(h-1)
    return node

root = build_tree(25)
# root = build_tree(25) # took 3.5 gb of ram for this..
# root = build_tree(30)
print('program finished..')