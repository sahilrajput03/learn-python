# Expect some magic from python, but it won't do magic but shows reality!


def a(aVar):
    print("I am function a,", aVar)
    aVar = 11


# ^^ this will only change the value of aVar in function a's scope only AND will not change the value of aVar of myFun's scope.


def myFun():
    aVar = 10
    a(aVar)
    print(
        "I am function b,", aVar
    )  # Here the value will remain 10 only, and its just same behaviour as javascript! NOTHING NEW!


myFun()
