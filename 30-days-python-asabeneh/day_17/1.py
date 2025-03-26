# try:
#       code in this block if things go well
# except: # (May or may not have a condition)
#       code in this block run if things go wrong

try:
    name = input("Enter your name:")
    year_born = input("Year you born:")
    age = 2019 - int(year_born)
    print(f"You are {name}. And your age is {age}.")
except TypeError:
    print("Type error occur")
except ValueError:
    print("Value error occur")
except ZeroDivisionError:
    print("zero division error occur")
else:  # This runs without when there is no exception:
    print("I usually run with the try block")
finally:
    print("I alway run.")
