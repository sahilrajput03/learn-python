secret_number = 7 # right number

count = 1

allowed_attempts = 3

def game(count):
  i = int(input(f'You have {allowed_attempts} attempts to guess the number. \nTry your luck, choose a number:\n'))
  count += 1
  if i == secret_number:
    print('Hooray..!')
  else:
    if count > allowed_attempts:
      print('Sorry, You loose!!')
      return # terminate the function execution.
    game(count)

# Start the game
game(count)