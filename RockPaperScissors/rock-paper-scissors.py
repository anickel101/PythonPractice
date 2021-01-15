import random

def game():

    ai_score = 0
    player_score = 0
    round = 0
    playing = 1

    game_prompt()
    scoreboard(round, ai_score, player_score)

    while playing > 0:
        winner = compare_moves()
        if winner == 1:
            print ("Player wins!")
            player_score += 1
        elif winner == -1:
            print ("Computer wins!")
            ai_score +=1
        else:
            print ("Tie Game!")
        
        scoreboard(round, ai_score, player_score)
        
        playing = nextRound()

def game_prompt():
    print ("Hello! Welcome to Rocks, Paper, Scissors...Shoot!")

def scoreboard(round, ai_score, player_score):
    print ("Round: {}".format(round))
    print ("Computer: {}".format(ai_score))
    print ("You: {}".format(player_score))

def compare_moves():
    ai = moveAI()
    player = movePlayer()
    printMove("Computer", ai)
    printMove("You", player)
    winner = 1
    if ai == 1:
        if player == 2:
            winner = 1
        elif player == 3:
            winner = -1
    elif ai == 2:
        if player == 1:
            winner = -1
        elif player == 3:
            winner = 1
    elif ai == 3:
        if player == 1:
            winner = 1
        elif player == 2:
            winner = -1
    else:
        winner = 0

    return winner

def moveAI():
    move = random.randint(1,3)
    return move

def movePlayer():
    tries = 1
    while tries > 0:
        m = int(raw_input("Choose [1] for Rocks, [2] for Paper, or [3] for Scissors..."))
        if m == 1 or m == 2 or m == 3:
            print m
            tries = 0
            return m
        else:
            print ("Invalid entry...")

def printMove(player, move):
    if move == 1:
        print ("{} chose Rocks!".format(player))
    elif move == 2:
        print ("{} chose Paper!".format(player))
    else:
        print ("{} chose Scissors!".format(player))

def nextRound():
    tries = 1
    while tries > 0:
        move = raw_input("Play Again? (y/n)")
        if move == 'y':
            tries = 0
            return 1
        elif move == 'n':
            tries = 0
            return -1
        else:
            print ("Invalid entry...")

game()