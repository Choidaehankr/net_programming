from random import randint
from urllib.request import OpenerDirector
secret_num = randint(1, 100)
num_guesses = 0
guess = 0

while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100): '))
    num_guesses = num_guesses + 1
    if guess < secret_num:
        print('더 커용', 5-num_guesses, '회 남았습니다.\n')
    elif guess > secret_num:
        print('더 작아용!', 5-num_guesses, '회 남았습니다.\n')
    else:
        print('맞았어용!')

if num_guesses == 5 and guess != secret_num:
    print('당신은 졌슴니당. 정답은! ', secret_num, '입니당!')