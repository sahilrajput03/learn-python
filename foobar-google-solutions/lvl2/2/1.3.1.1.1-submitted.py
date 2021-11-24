height = 0
# NOTE THERE SHOULDN'T BE ANY PRINT STATEMENTS IN THE PROGRAM ELSE THE TESTS WON'T GET VERIFIED AT ALL!
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

count = 0
def visitInPostOrder(root):
    if root:
        visitInPostOrder(root.left)
        visitInPostOrder(root.right)
        global count
        count = count + 1
        root.gglValue = count
        # print('gglValue', root.gglValue,', our tree', root.data)
        # if(root.gglValue == 19 ): print('19 -> ', root.)

rootElement = None

def getParent(root, target):
    # global printParent
    if printParent(root, target) is None:
        printParent(root, target)
        return rootElement
    else:
        return -1        

def printParent(root, target):
    global rootElement
    if root == None:
        return False
    if root.gglValue == target:
        return True
    # If target is present in tree, then prints the parent node
    leftHasTarget = printParent(root.left, target)
    rightHasTarget = printParent(root.right, target)
    if (leftHasTarget or rightHasTarget):
        rootElement = root.gglValue
        # print('getParent:',rootElement)



def solution(inputHeight, list):
    global height
    height = inputHeight

    root = build_tree(height)
    # print('build pefect tree of height', height) 
    visitInPostOrder(root)

    p = []

    for i in list:
        p.append(getParent(root, i))

    # print(p)
    return p

solution(3, [7,3,5,1])
# FYI.., please comment above to make below function call work good!
# solution(5, [19, 14, 28])





# A function to do postorder tree traversal
 
# ##############


# print('\nPrinting parent value..')
# testing new fun..!
# getParent(root, 3)
# print(printParent(root, 1))

# for height 3
# print(getParent(root, 7)) # solution: -1
# print(getParent(root, 3)) # solution: 7
# print(getParent(root, 5)) # solution: 6
# print(getParent(root, 1)) # solution: 3


# # for height 5
# print(getParent(root, 19)) # solution: 21
# print(getParent(root, 14)) # solution: 15
# print(getParent(root, 28)) # solution: 29