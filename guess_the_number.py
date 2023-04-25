from random import randint


def guess_the_number():
    print('Guess the number game!')
    # Choosing range of random numbers
    while True:
        try:
            first = int(input('Chose start of range '))
            second = int(input('Chose end of range '))
            if first > second:
                print('Incorrect input, first number is higher than second, try again.')
            else:
                break
        except ValueError:
            print('Not a number!')

    # Question for the player, if in need of help while guessing
    need_help = input('Do you need help while guessing? (Y/N) ')
    while not (need_help == 'Y' or need_help == 'N'):
        print('Wrong input')
        need_help = input('Do you need help while guessing? (Y/N) ')

    # Limiting or not number of guesses
    while True:
        try:
            tries = int(input('How many guesses do need? If you would like unlimited number of guesses enter "0"'))
            break
        except ValueError:
            print('Not a number!')

    number = randint(int(first), int(second))

    # Game without help, with limited answers
    if need_help == 'N' and tries != 0:
        while tries != 0:
            try:
                guess = int(input('Take a guess: '))
                if guess == number:
                    print(f'You guessed it, congrats!')
                    break
                else:
                    tries -= 1
                    print(f'Try again, you have {tries} tries')
                if tries == 0:
                    print('Game over, you used all your tries')
            except ValueError:
                print('Not a number!')

    # Game with help and unlimited number of tries
    elif need_help == 'Y' and tries == 0:
        while True:
            try:
                guess = int(input('Take a guess: '))
                if guess == number:
                    print(f'You guessed it, congrats!')
                    break
                elif guess > number:
                    print('Try again, number that you are guessing is smaller')
                elif guess < number:
                    print('Try again, number that you are guessing is bigger')
                else:
                    continue
            except ValueError:
                print('Not a number!')

    # Game with help and limited number of tries
    elif need_help == 'Y' and tries != 0:
        while tries != 0:
            try:
                guess = int(input('Take a guess: '))
                if guess == number:
                    print(f'You guessed it, congrats!')
                    break
                elif guess > number:
                    tries -= 1
                    print(f'Try again, number that you are guessing is smaller, you have {tries} tries')
                elif guess < number:
                    tries -= 1
                    print(f'Try again, number that you are guessing is bigger, you have {tries} tries')
                else:
                    continue
                if tries == 0:
                    print('Game over, you used all your tries')
            except ValueError:
                print('Not a number!')

    # Game without help and unlimited number of tries
    else:  # (help == 'N' and tries == 0):
        while True:
            try:
                guess = int(input('Take a guess: '))
                if guess == number:
                    print(f'You guessed it, congrats!')
                    break
                else:
                    print('Try again')
            except ValueError:
                print('Not a number!')


while True:
    guess_the_number()
    go_again = input('Wanna play again? Y/N: ')
    while not (go_again == 'Y' or go_again == 'N'):
        print('Wrong input')
        go_again = input('Wanna play again? Y/N: ')
    if go_again == 'N':
        break
    else:
        continue