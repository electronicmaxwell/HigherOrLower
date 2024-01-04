import random
import time


def display_score(num):
    if count != 2:
        return f' Your score is now {num}!'
    else:
        return ''


def is_valid_input(dic, var):
    while True:
        var = var.strip().lower()
        if var in dic.keys():
            return dic[var]
        else:
            print('*ERROR*')
            time.sleep(1)
            if len(dic) == 4:
                print('Your input must be yes or no.')
                time.sleep(1)
                print('Examples of viable inputs are no, YeS, n, Y')
            else:
                print('Your input must be a number or written number between 0 and 10.')
                time.sleep(1)
                print('Examples of viable inputs are 5, five, TEN, sEVeN.')
            time.sleep(1)
            var = input('Please try again\n')


yes_no_dict = {
    'yes': True,
    'y': True,
    'no': False,
    'n': False
}

num_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}

rules = is_valid_input(yes_no_dict, input('Welcome to Higher or Lower! Would you like to see the rules? \n'))
time.sleep(1)
if rules:
    print('''The rules are as follows...
I, your computer, will think of a number between 0 and 10 (including both).
You, the player, will then try to guess my number. If you get it on the first try you will get 10 points!
If you fail to guess on your first try, I will let you know whether my number is higher or lower than your guess.
You will then try to guess again. If you guess my number on your second attempt you will get 5 points.
If you fail to guess my number within 2 attempts, you will get no points.
There will be 3 rounds of this. If after 3 rounds you have scored 15 or more points, you win!''')
    time.sleep(5)
    print('The game will begin shortly \n')
    time.sleep(2)


play = True
while play:
    count = 0
    score = 0
    while count < 3:
        print(f'Get ready for round {count+1}')
        time.sleep(1)
        num_2_guess = random.randint(0,10)
        print('I am thinking of a number between 0 and 10.')
        time.sleep(1)
        guess = is_valid_input(num_dict, input('Can you guess it?\n'))
        if guess == num_2_guess:
            score += 10
            time.sleep(1)
            print(f'Congrats! You guessed correctly!{display_score(score)}')
            time.sleep(1)
        else:
            if num_2_guess > guess:
                higher_lower = 'higher'
            else:
                higher_lower = 'lower'

            time.sleep(1)
            print(f'Not quite! The number I am thinking of is {higher_lower} than {guess}.')
            time.sleep(1)
            second_guess = is_valid_input(num_dict, input('Can you guess it now?\n'))
            if second_guess == num_2_guess:
                score += 5
                time.sleep(1)
                print(f'Nice guess! You got it correct!{display_score(score)}')
                time.sleep(1)
            else:
                time.sleep(1)
                print(f'Unlucky! You got no points for this round. '
                      f'I was thinking of the number {num_2_guess}.{display_score(score)}')
                time.sleep(1)
        count += 1

    print('The game is now over. You needed 15 points to win and you scored...')
    time.sleep(2)
    if score >= 15:
        print(f'{score}!')
        time.sleep(1)
        print('Congratulations you won!')
    else:
        print(f'{score} :(')
        time.sleep(1)
        print('You lost. Better luck next time.')

    play = is_valid_input(yes_no_dict, input('Would you like to play again?\n'))
