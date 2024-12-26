# All below if statements resolve to true.

if type(10) == int:
    print("integer type")

if type(3.14) == float:
    print("float type")

if type(1 + 3j) == complex:
    print("complex type")

if type([1,2,3]) == list:
    print("list type")

if type({9.8, 3.14, 2.7}) == set:
    print("set type")

if type((9.8, 3.14, 2.7)) == tuple:
    print("tuple type")
print()


# ############
# check variable type using `isinstance`
if isinstance(10, int):
    print("integer type")

if isinstance(3.14, float):
    print("float type")

if isinstance(1 + 3j, complex):
    print("complex type")

if isinstance([1,2,3], list):
    print("list type")

if isinstance({9.8, 3.14, 2.7}, set):
    print("set type")

if isinstance((9.8, 3.14, 2.7), tuple):
    print("tuple type")
print()