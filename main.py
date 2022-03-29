import numpy as np

a = np.array([['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']])
acceptable_values = 'The acceptable values are: (00) (01) (02) ' \
                    '       (10) (11) (12) ' \
                    '       (20) (21) (22)'


def printing_array():
    for line in a:
        print(f"  {' | '.join(map(str, line))}  ")
        print("----------")


def add_values(pos, player):
    """ pos: position in the array that the player input
        player: which player is playing
    """
    if player == 1:
        (a[int(pos[0])][int(pos[1])]) = "X"
    else:
        (a[int(pos[0])][int(pos[1])]) = "O"


def check_values(pos):
    """pos: position in the array that the player input
        It checks for the win condition
    """
    # checking if the column has 3 same values
    col = a[:, int(pos[1])]
    if col[0] == col[1] == col[2]:
        return True

    # checking if the row has 3 same values
    row = a[int(pos[0]), :]
    if row[0] == row[1] == row[2]:
        return True

    # checking if the diagonal has 3 same values
    diag = np.diagonal(a, offset=0, axis1=1, axis2=0)
    if "*" in diag:
        pass
    elif diag[0] == diag[1] == diag[2]:
        return True

    # checking if the reverse diagonal has 3 same values
    diag_flip = np.fliplr(a).diagonal()
    if "*" in diag_flip:
        pass
    elif diag_flip[0] == diag_flip[1] == diag_flip[2]:
        return True


def game_flow(pos, player):
    """ pos: position in the array that the player input
            player: which player is playing
            this function does a lot of stuff
        """

    # checking if the input enter is numeric, doesnt violate the index range of the array, and the length is not
    # less than 2 or greater than 2
    if len(pos) == 2 and pos.isnumeric() and int(pos[0]) < 3 and int(pos[1]) < 3:
        # this check prevents user from inserting value in an already filled space
        if a[int(pos[0])][int(pos[1])] == "*":
            add_values(pos, player)
            printing_array()
            signal = check_values(pos)
            return signal
        else:
            print('the place is already filled, try again with other value')
            if player == 1:
                player1()
            else:
                player2()
    else:
        # feedback if the input is wrong
        print(f"Please enter the correct position. {acceptable_values}")
        if player == 1:
            player1()
        else:
            player2()


def player1():
    x_pos = (input("Player 1: "))
    signal = game_flow(x_pos, 1)
    return signal


def player2():
    o_pos = (input("Player 2: "))
    signal = game_flow(o_pos, 2)
    return signal


def check_for_draw():
    if "*" not in a:
        return True


print(" TIC TAC TOE GAME - TEXT VERSION")
print(" PLAYER 1: X")
print(" PLAYER 2: O")
printing_array()
print(acceptable_values)

keep_playing = False
while keep_playing != True:
    if check_for_draw():
        winner = "draw"
        break
    keep_playing = player1()
    if keep_playing:
        winner = "Player 1"
        break
    else:
        if check_for_draw():
            winner = "draw"
            break
        else:
            keep_playing = player2()
            winner = "Player 2"


if winner == "draw":
    print("Its a DRAW")
else:
    print(f"The winner is {winner} ")
