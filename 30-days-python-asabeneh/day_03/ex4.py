# Write a script that prompts the user to enter number of years. Calculate the
# number of seconds a person can live. Assume a person can live hundred years
# SAMPLE:
#   Enter number of years you have lived: 100
#   You have lived for 3153600000 seconds.


years = int(input("Enter number of years you have lived: "))  # assuming input 100
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

print(3153600000 == seconds)  # True (assuming we entered `years = 100`)
