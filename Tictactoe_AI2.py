import random
Board2=[[0 for j in range(3)] for i in range(3)]
Board=[[0 for j in range(3)] for i in range(3)]

def printboard():
    for i in range(3):
        print(Board[i])

def checkit(a):
    if((Board[0][0]==a)&(Board[0][1]==a)&(Board[0][2]==a)):
       print(a,'wins')
def checkfull():
    full=1
    for i in range(3):
        for j in range(3):
            if(Board[i][j]==0):
                full=0
    return full

def playAI2():
    flag=checkfull()
    while(flag==0):
        k=random.randint(1,9)
        i=int((k-1)/3)
        j=k-1-3*i
        if(Board[i][j]==0):
            Board[i][j]=2
            flag=1

printboard()
full=0
while(full==0):
    move=input()
    player=1
    Board[int(move[0])][int(move[1])]=player
    printboard()
    print('Player2')
    playAI2()
    printboard()
    print('Player1')
    checkit(1)
    full=checkfull()
