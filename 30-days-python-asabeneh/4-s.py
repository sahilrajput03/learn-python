# Get no. of user.
# max no. of attempt 3.

target = 7 # right no.

count = 1

def game(count):
  i = int(input('Try your luck, choose a number..\n'))
  count += 1
  if i == target:
    print('Hooray..!')
  else:
    if count > 3:
      print('Sorry, You loose!!')
      return
      # ^^ terminate the function execution.
    game(count)

# start the game...
game(count)