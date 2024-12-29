info = """
start - to start the car
stop - to stop the car
quit - to exit
"""

welcome_message = """🤠︎ Welcome to the game!"""

print(welcome_message, info)


def game(is_started):
    choice = input().lower()
    if choice == "help":
        print(info)
        game(is_started)
    elif choice == "start":
        if is_started == True:
            print("You car is already started🥶︎!")
            game(is_started)
        print("Your car started..🚀︎🚀︎!!.")
        is_started = True
        game(is_started)
    elif choice == "stop":
        if is_started == False:
            print("You car is already stopped🥶︎!")
            game(is_started)
        print("You car stopped ..🛑︎🛑︎")
        is_started = False
        game(is_started)
    elif choice == "quit":
        print("Thanks for playing the game 🧸︎")
        return
    else:
        print("I don't understand that...")
        print("Try again..")
        game(is_started)


game(False)

# Some case flow of this game:
"""
CASE: If user types any wrong choice..!
print >>> I don't understand that...

CASE: If choose start
Car started...Ready to go!

CASE: If choose stop
Car stopped.
"""
