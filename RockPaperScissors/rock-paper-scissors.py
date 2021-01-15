import random

ai_score = 0
player_score = 0
round = 1
again = True

def game_prompt():
    print ("Hello! Welcome to Rocks, Paper, Scissors...Shoot!")

def moveAI():
    move = random.randint(1,3)
    return move

def movePlayer():
    m = int(raw_input("Choose [1] for Rocks, [2] for Paper, or [3] for Scissors..."))
    print m
    return m

def printMove(player, move):
    if move == 1:
        print ("{} chose Rocks!".format(player))
    elif move == 2:
        print ("{} chose Paper!".format(player))
    else:
        print ("{} chose Scissors!".format(player))

def compare_moves(ai_score, player_score):
    ai = moveAI()
    player = movePlayer()
    printMove("Computer", ai)
    printMove("You", player)
    if ai == 1:
        if player == 2:
            player_score += 1
        elif player == 3:
            ai_score += 1
    elif ai == 2:
        if player == 1:
            ai_score += 1
        elif player == 3:
            player_score += 1
    elif ai == 3:
        if player == 1:
            player_score += 1
        elif player == 2:
            ai_score += 1


def play():
    while again == True:
        compare_moves(ai_score, player_score)
        scoreboard()
        nextRound()

def nextRound():
    move = raw_input("Play Again? (y/n)")
    if move == 'y':
        again = True
    else:
        again = False

def scoreboard():
    print ("Computer: {}".format(ai_score))
    print ("You: {}".format(player_score))

def game():
    game_prompt()
    scoreboard()
    play()

game()