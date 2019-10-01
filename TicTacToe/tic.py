# import Files

# Create Board list
board=[' ' for x in range(10)]

# Method to add letter at perticular Position
def inserLetter(letter, pos):
    board[pos] = letter

# check whether Space is free
def spaceIsFree(pos):
    return board[pos] == ' '

# Create Board / Print Board
def printBoard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('___|___|___')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('   |   |   ')

# check the Board is Full
def isBoardFull(board):
    if (board.count(' ') > 1 ):
        return False
    else:
        return True

# check if winner
def isWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

# Create player turn
def playerTurn():
    run = True
    while run:
        move = input("Enter a position between 1 to 9 where you want to play : ")

        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    inserLetter('X', move)
                else:
                    print("Sorry this place is already occupied")
            else:
                print("Please enter a number between 1 and 9")
        except:
            print("Please type a Number :")

# Create Computer Turn
def ComputerTurn():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandomCorner(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

 # Generate a Random

def selectRandomCorner(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

# Main Logic
def main():
    print("***************************************************** ")
    print("***************** Welcome to Game! ****************** ")
    print("***************************************************** ")
    print("=====================================================")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerTurn()
            printBoard(board)
        else:
            print("Sorry You Loose")
            break

        if not(isWinner(board,'X')):
            move = ComputerTurn()
            if move == 0:
                print(" ")
            else:
                inserLetter('O',move)
                print("Computer Places an O on Position ", move , ':')
                printBoard(board)
        else:
            print("You win !!!")
            break

# If the board Is Board Full
    if isBoardFull(board):
        print('Tie Game!!!')


while True:
    print("=====================================================")
    x = input ("Do you want to Play Tic Tac Toe with Me??? (y/n)  :")
    print("=====================================================")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("=====================================================")
        main()
    else:
        break
# Is Board Full
