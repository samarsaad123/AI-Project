from copy import deepcopy
board = []

with open('puzzle.txt','r') as f:
    for line in f:
        board.append(line.strip().split(' '))


def print_puzzle(p):
    str = ''
    for i in range(3):
        for j in range(3):
            if p[i][j] == '0':
                str += '  '
            else:
                str += p[i][j] + ' '
        str += '\n'
    print(str)

class puzzle:
    def __init__ (self, starting, parent):
        self.board = starting
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

    def manhattan(self):
        A = 0
        h = 0
        for i in range(3):
            for j in range(3):
                h += abs(A - self.board[i][j])
            A += 1
        return h
    def goal(self):
        A = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != A:
                    return False
                A += 1
        return True

    def __eq__(self, other):
        return self.board == other.board

def move_function(curr):
    curr = curr.board
    #print(curr,"r")
    for i in range(3):
        for j in range(3):
            if curr[i][j] == 0:
                x, y = i, j
                break
    q = []
    if x-1 >= 0:
        b = deepcopy(curr)

        b[x][y]=b[x-1][y]
        b[x-1][y]=0
        succ = puzzle(b, curr)
        q.append(succ)
    if x+1 < 3:
        b = deepcopy(curr)

        b[x][y]=b[x+1][y]
        b[x+1][y]=0
        succ = puzzle(b, curr)
        q.append(succ)
    if y-1 >= 0:
        b = deepcopy(curr)

        b[x][y]=b[x][y-1]
        b[x][y-1]=0
        succ = puzzle(b, curr)
        q.append(succ)
    if y+1 < 3:
        b = deepcopy(curr)

        b[x][y]=b[x][y+1]
        b[x][y+1]=0
        succ = puzzle(b, curr)
        q.append(succ)

    return q

def best_fvalue(openList):
    f = openList[0].f
    #print(f,"h")
    index = 0
    for i, item in enumerate(openList):
        if i == 0:
            continue
        if(item.f < f):
            #print(item.f,"l")
            f = item.f
            index  = i

   # print(openList[index],"hi")

    return openList[index], index

def AStar(start):

    openList = []
    closedList = []
    openList.append(start)

    while openList:
        current, index = best_fvalue(openList)
        if current.goal():
            return current
        openList.pop(index)
        #print(openList,"i")
        closedList.append(current)

        X = move_function(current)
        #print(X, "yiusef")
        for move in X:
            ok = False   #checking in closedList
            for i, item in enumerate(closedList):
                if item == move:
                    ok = True
                    break
            if not ok:              #not in closed list
                newG = current.g + 1
                present = False

                #openList includes move
                for j, item in enumerate(openList):
                    if item == move:
                        present = True
                        if newG < openList[j].g:
                            openList[j].g = newG
                            openList[j].f = openList[j].g + openList[j].h
                            openList[j].parent = current
                if not present:
                    move.g = newG
                    move.h = move.manhattan()
                    move.f = move.g + move.h
                    move.parent = current
                    openList.append(move)

    return None


#start = puzzle([[2,3,6],[0,1,8],[4,5,7]], None)
#print(start,"a")
start = puzzle([[1,0,2],[3,4,5],[6,7,8]], None)
# start = puzzle([[0,1,2],[3,4,5],[6,7,8]], None)
#start = puzzle([[1,2,0],[3,4,5],[6,7,8]], None)
result = AStar(start)
noofMoves = 0
arr=[]

if(not result):
    print ("No solution")
else:
    print (result.board)
    t=result.parent
    i=0
    #print(t.board)
    while t:
        i+=1
        noofMoves += 1
        print(t.board)
        t=t.parent
print ("Length: " + str(noofMoves))