from random import randint

global coin

coin = 50


while True:
    num = randint(1, 2)
    x = int(input('앞면(1) / 뒷면(2): '))
    if(num == x):
        coin -= 9
    else:
        coin -= 10
    print('now coin value: ', coin)
    if coin < 0 or coin >= 100:
        break