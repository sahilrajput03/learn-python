a = 11
b = 22

def c():
    global a # global a toh dena pdega, raaj hi chlega!
    a = 99
    b = 99

c()
print(a)
print(b)