import sys
from random import randint

def genChilds(x):
    childs = []
    for k in range(len(x)):
        for i in range(x[k]):
            c = x[:k] + (i,) + x[k+1:]
            childs.append(c)
    return childs

class Solver:
    def __init__(self, size):
        self.db = dict()
        ground_case = tuple([0 for _ in range(size)])
        self.db[ground_case] = True
    def isWin(self, x):
        childs = genChilds(x)
        #print("x = " + str(x) + ", childs = " + str(childs))
        for c in childs:
            #print("checking childs = " + str(c))
            if not self.db.has_key(c):
                self.db[c] = self.isWin(c)
            if not self.db[c]:
                    return True
        return False
    def move(self, x):
        childs = genChilds(x)
        for c in childs:
            if not self.db.has_key(c):
                self.db[c] = self.isWin(c)
            if not self.db[c]:
                return c
        print("Computer: Actually you win, if you are smart enough :)")
        # Return random child to x
        return childs[0]

if __name__ == '__main__':
    N = 3
    M = 1000 
    S = Solver(N)
    x = tuple([randint(1,M) for _ in range(N)])
    base_case = tuple([0 for _ in range(N)])
    #w = S.isWin(x)
    #print(str(x) + " is win = " + str(w))
    #print("next = " + str(nextX))
    player = 0
    while x != base_case:
        print(x)

        possibleMoves = genChilds(x)
        # Players turn
        player_ok = False
        while not player_ok:
            player_ok = True
            s = raw_input("You: ")
            nextX = [y for y in s.split(' ') if y]
            try:
                nextX = tuple([int(y) for y in nextX])
            except:
                print("Could not parse input '" + s + "', try again!")
                player_ok = False

            if len(nextX) != N:
                print("Input '" + s + "' must be of length " + str(N) + ", try again!")
                player_ok = False

            if not nextX in possibleMoves:
                print("Move '" + s + "' invalid, can only decrease one at a time! try again!")
                player_ok = False

        if nextX == base_case:
            print("You lose!")
            sys.exit(0)

        # Computer turn
        x = S.move(nextX)
        print("Computer: " + str(x))
        
    print("You win!")
    sys.exit(0)
