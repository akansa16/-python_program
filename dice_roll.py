import random
def main():
    player1=0
    player1wins=0
    player2=0
    player2wins=0
    rounds=1
    while rounds!=10:
        print("round"+str(rounds))
        player1=dice_roll()
        player2=dice_roll()
        print("player 1 roll :"+str(player1))
        print("player 2 roll :"+str(player2))
        if player1==player2:
            print("draw!\n")
        elif player1 > player2:
            player1wins = player1wins+1
            print("player 1 wins\n")
        else:
            player2wins=player2wins + 1
            print("player 2 wins!\n")
        rounds=rounds + 1
    if player1wins==player2wins:
     print("draw!")
    elif player1wins > player2wins:
     print("player 1 wins no.of rounds won :" + str(player1wins))
    else:
         print("player 2 wins no.of  rounds won :" + str(player2wins))
def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll
main()