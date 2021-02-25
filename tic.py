print('''---------
|       |
|       |
|       |
---------''')

win = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
       [0, 3, 6], [1, 4, 7], [2, 5, 8],
       [0, 4, 8], [2, 4, 6]]


def output(symbol):
    for sets in win:
        count = 0
        for num in sets:
            if board[num] == symbol:
                count += 1
        if count == 3:
            return True


count = 0
cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
A = "QABCDEFGHIJKLMNOPRSTUVYZXWabcdefghijklmnoprstuvyzxwq"
for i in range(0, 9):
    coordinates = input("Enter the coordinates: ")
    if coordinates[0] in A:
        print("You should enter numbers!")
    elif coordinates[2] in A:
        print("You should enter numbers!")
    elif int(coordinates[0]) > 3 or int(coordinates[0]) < 1:
        print("Coordinates should be from 1 to 3!")
    elif int(coordinates[2]) > 3 or int(coordinates[2]) < 1:
        print("Coordinates should be from 1 to 3!")
    else:
        movein = (((int(coordinates[0]) - 1) * 3) + (int(coordinates[2]) + 2)) - 3
        if cells[movein] == ' ':
            cells[movein] = "X"
            board = ''.join(map(str, cells))
            print(board)
            print("---------")
            print("| " + board[0] + " " + board[1] + " " + board[2] + " |")
            print("| " + board[3] + " " + board[4] + " " + board[5] + " |")
            print("| " + board[6] + " " + board[7] + " " + board[8] + " |")
            print("---------")

            if output('X'):
                print('X wins')
                break
            elif output('O'):
                print('O wins')
                break

            elif board.count(' ') == 0:
                print('Draw')
                break


        else:
            print("This cell is occupied! Choose another one!")

    coordinates = input("Enter the coordinates: ")
    if coordinates[0] in A:
        print("You should enter numbers!")
    elif coordinates[2] in A:
        print("You should enter numbers!")
    elif int(coordinates[0]) > 3 or int(coordinates[0]) < 1:
        print("Coordinates should be from 1 to 3!")
    elif int(coordinates[2]) > 3 or int(coordinates[2]) < 1:
        print("Coordinates should be from 1 to 3!")
    else:
        movein = (((int(coordinates[0]) - 1) * 3) + (int(coordinates[2]) + 2)) - 3
        if cells[movein] == ' ':
            cells[movein] = "Y"
            board = ''.join(map(str, cells))
            print(board)
            print("---------")
            print("| " + board[0] + " " + board[1] + " " + board[2] + " |")
            print("| " + board[3] + " " + board[4] + " " + board[5] + " |")
            print("| " + board[6] + " " + board[7] + " " + board[8] + " |")
            print("---------")
            if output('X'):
                print('X wins')

            elif output('O'):
                print('O wins')

            elif board.count(' ') == 0:
                print('Draw')
            count += 1
        else:
            print("This cell is occupied! Choose another one!")
            if output('X'):
                print('X wins')
                break
            elif output('O'):
                print('O wins')
                break

            elif board.count(' ') == 0:
                print('Draw')
                break
