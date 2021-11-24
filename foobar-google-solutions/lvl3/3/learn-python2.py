# print([None for i in range(3)])
# Output: [None, None, None]

print([[None for i in range(3)] for i in range(5)])
# Output: [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]