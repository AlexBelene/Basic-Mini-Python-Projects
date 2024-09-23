### 🎰 Guess The Number with Zahari Baharov 

![](images/img16x9_1414835806.jpg)

### 🍀 Project Overview 

In "Guess A Number," you’ll compete against the computer! Here’s how it works:

1. The computer randomly selects a number between 1 and 100.
2. You have 3 attempts to guess this number.
3. After each guess, the computer will provide a hint: whether the target number is greater or less than your guess.
4. Your goal is to guess the correct number within the allotted attempts!
   
At the end of the game, you’ll have the option to play again. 
### 💵 Are you ready to test your guessing skills?

```python
import random

computer_number = random.randint(1, 100)

try_counter = 0

while True:
    if try_counter > 3:
        print('You have exceeded the maximum number of attempts (3), game over!')
        break

    player_input = input('Guess the number (1-100): ')

    if not player_input.isdigit():
        print('Not a number, please choose a number (1-100): ')
        continue

    player_input = int(player_input)

    if player_input == computer_number:
        print('Congratulations, you guessed the correct number!\nDo you want to play again?')

        play_again = input('(yes/no): ').strip()
        if play_again.lower() == 'yes':
            continue
        elif play_again.lower() == 'no':
            break

    elif player_input > computer_number:
        print('To High of a Number, try again!')
        try_counter += 1
    else:
        print('To Low of a Number, try again!')
        try_counter += 1

```

