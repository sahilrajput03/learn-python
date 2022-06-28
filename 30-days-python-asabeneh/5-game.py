print("""🤠︎ Welcome to the game
Infomation:
Start - to start the car
stop - to stop the car
quit - to exit
help - car manual""")

info = """Start - to start the car
stop - to stop the car
quit - to exit

CASE: If user types any wrong choice..!
print >>> I don't understand that...

CASE: If choose start
Car started...Ready to go!

CASE: If choose stop
Car stopped."""
isCarStarted = False

def game(isCarStarted):
  choice = input().lower()
  if choice == 'help':
    print(info)
    game(isCarStarted)
  elif choice == 'start':
    if isCarStarted == True:
      print('You car is already started🥶︎!')
      game(isCarStarted)
    print('Your car started..🚀︎🚀︎!!.')
    isCarStarted = True
    game(isCarStarted)
  elif choice == 'stop':
    if isCarStarted == False:
      print('You car is already stopped🥶︎!')
      game(isCarStarted)
    print('You car stopped ..🛑︎🛑︎')
    isCarStarted = False
    game(isCarStarted)
  elif choice == 'quit':
    print('Thanks for playing the game 🧸︎')
    return
  else:
    print("I don't understand that...")
    print('Try again..')
    game(isCarStarted)

game(isCarStarted)