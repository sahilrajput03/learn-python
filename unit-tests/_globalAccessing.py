v1 = 10

def f1():
    global v1 # Try commenting this line and see the side-effect.
    v1 = 20

f1()

print(v1)