# Shorter version of above code:
try:
    name = input("Enter your name:")
    year_born = input("Year you born:")  # * Try inputing string here to trigger error.
    age = 2025 - int(year_born)
    print(f"You are {name}. And your age is {age}.")
except Exception as e:  # * Catching all exceptions in a single instruction.
    print("Sorry we got exception:", e)
