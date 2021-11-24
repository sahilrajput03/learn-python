from collections import deque 
      
# Declaring deque 
queue = deque(['name','age','DOB'])  
      
print(queue)
print(queue.popleft())
print(queue)

###############
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
a = []
a.append(5)
a.append(4)
a.append(3)
print("Hello world", a)
poppedItem = a.pop(0) #LEARN python: a.pop() would have popped the right-most item.
print("Hello world", a)
print('poppedItem', poppedItem)
# output: 
# Hello world [5, 4, 3]
# Hello world [4, 3]
# poppedItem 5