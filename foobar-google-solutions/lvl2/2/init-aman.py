class Node:
   def __init__(self, data=None):
    self.data = data
    self.nextNode = None
    
class SLinkedList:
   def __init__(self):
      self.rootNode = None

   def printLL(self):
      printval = self.rootNode
      while printval is not None:
         print (printval.data)
         printval = printval.nextNode

mySingleLL = SLinkedList()
mySingleLL.rootNode = Node("Mon")

# creating two nodes.
tuesdayNode = Node("Tue")
wednesdayNode = Node("Wed")

# Link first Node to second node
mySingleLL.rootNode.nextNode = tuesdayNode

# Link second Node to third node
tuesdayNode.nextNode = wednesdayNode

mySingleLL.printLL()