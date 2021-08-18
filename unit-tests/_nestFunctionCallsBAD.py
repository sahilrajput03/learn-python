
def myFun():
    aVar = 10
    def a():
        print('I am function a,', aVar)
        aVar = 11

    
    a()
    print('I am function myFun,', aVar)


myFun()
