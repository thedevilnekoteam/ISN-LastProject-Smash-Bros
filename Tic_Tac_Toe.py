# Python Tic Tac Toe Game
import random
# The Game Board


def check(c, p1, p2, p3):
    if board[p1] == c and board[p2] == c and board[p3] == c:
        return "Win"


def check1(c):
    if check(c, 0, 1, 2) == "Win":
        return "Win"
    elif check(c, 3, 4, 5) == "Win":
        return "Win"
    elif check(c, 6, 7, 8) == "Win":
        return "Win"
    elif check(c, 0, 3, 6) == "Win":
        return "Win"
    elif check(c, 2, 5, 8) == "Win":
        return "Win"
    elif check(c, 1, 4, 7) == "Win":
        return "Win"
    elif check(c, 0, 4, 8) == "Win":
        return "Win"
    elif check(c, 2, 4, 6) == "Win":
        return "Win"


def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+---")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+---")
    print(board[6], "|", board[7], "|", board[8])


board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

show()

while True:
    ch = int(input("Choose a spot: "))

    while ch < 0 or ch > 8:
        ch = int(input("Choose a spot: "))

    if board[ch] != "x" and board[ch] != "o":
        board[ch] = "x"

        if check1("x") == "Win":
            print("User Win!")
            show()
            break

        ch1 = random.randrange(0, 9)
        while board[ch1] == "x" or board[ch1] == "o":
            ch1 = random.randrange(9)
        if board[ch1] != "x" and board[ch1] != "o":
            board[ch1] = "o"
            if check1("o") == "Win":
                print("Console Win!")
                show()
                break

    else:
        print("This spot is taken!")
    show()
