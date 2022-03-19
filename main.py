import game
game.gameStart()
while True:
    if (input('是否繼續遊玩新一輪? y/n \n'))=='y':
        game.gameStart()
    else:
        break
