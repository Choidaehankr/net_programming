from random import randint


player_coin = int(50) #player가 처음에 가지고 있는돈 $50

while(1):
    coin = randint(1, 2) #동전을 한 번 던져서 나오는 랜덤 수 [앞면(1), 뒷면(2)]
    player = int(input('enter 1 or 2 : '))

    if player == coin: #player가 맞추면
        player_coin += int(9)
        print(player_coin)
        if player_coin <= 0:
            print("GAME OVER")
            break
        elif player_coin >= 100:
            print("당신의 승리")
            break
    elif player != coin: #player가 못 맞추면
        player_coin -= int(10)
        print(player_coin)
        if player_coin <= 0:
            print("GAME OVER")
            break
        elif player_coin >= 100:
            print("당신의 승리")
            break