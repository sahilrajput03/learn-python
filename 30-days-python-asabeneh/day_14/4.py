# & Accepting Parameters in Decorator Functions
# * Most of the time we need our functions to take parameters, so we might need to
# * define a decorator that accepts parameters.


def logLocationDecorator(logNameFn):
    def wrapper_accepting_parameters(para1, para2, para3):
        logNameFn(para1, para2, para3)  # `function` here is `printName` function
        print("I live in {}".format(para3))  # Log location

    return wrapper_accepting_parameters


@logLocationDecorator
def logName(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name, country))


logName("Asabeneh", "Yetayeh", "Finland")
