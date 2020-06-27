import random
Board2=[[0 for j in range(3)] for i in range(3)]
Board=[[0 for j in range(3)] for i in range(3)]

def printboard():
    for i in range(3):
        print(Board[i])

printboard()

for play in range(5):
    move=input()
    player=1
    Board[int(move[0])][int(move[1])]=player
    printboard()
    print('Player2')
    move=input()
    player=2
    Board[int(move[0])][int(move[1])]=player
    printboard()
    print('Player1')
