import random
computer_move = ''

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input(f"Choose [r]ock, [p]apaer or [s]cissors: ")

if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Try again...')


computer_random_number = random.randint(1, 3)

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f'The computer chose {computer_random_number} = {computer_move}')

if (player_move == rock and computer_move == scissors) or \
     (player_move == scissors and computer_move == paper) or \
     (player_move == paper and computer_move == rock):
    print('You win!')
elif player_move == computer_move:
    print('It\'s a tie!')
else:
    print('You lose!')
