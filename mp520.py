import copy
"""
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 
A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
"""
#vertical down
def vert_dow(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    for i in range(cr+1, tr):
        if state[i][cc] == ' ':
            break
        if state[i][cc] == player:
            bpos = i
            break
    if bpos != -1:
        return abs(bpos-cr)-1
    else:
        return 0

# for vertical upwards


def vert_up(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    for i in range(cr-1, -1, -1):
        if state[i][cc] == ' ':
            break
        if state[i][cc] == player:
            bpos = i
            break
    if bpos != -1:
        return abs(cr-bpos)-1
    else:
        return 0

# for horizontal right side


def hor_right(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    for i in range(cc+1, tc):
        if state[cr][i] == ' ':
            break
        if state[cr][i] == player:
            bpos = i
            break
    if bpos != -1:
        return abs(bpos-cc)-1
    else:
        return 0

# for horizontal left side


def hor_left(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    for i in range(cc-1, -1, -1):
        if state[cr][i] == ' ':
            break
        if state[cr][i] == player:
            bpos = i
            break
    if bpos != -1:
        return abs(cc-bpos)-1
    else:
        return 0

# for diagonal- left - top


def diag_left_top(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr-1
    tempc = cc-1
    while(tempr >= 0 and tempc >= 0):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bpos = tempr
            break
        tempr -= 1
        tempc -= 1
    if bpos != -1:
        return abs(cr-bpos-1)
    else:
        return 0

# for diagonal- right - top


def diag_right_top(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr-1
    tempc = cc+1
    while(tempr >= 0 and tempc < tc):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bpos = tempr
            break
        tempr -= 1
        tempc += 1
    if bpos != -1:
        return abs(cr-bpos)-1
    else:
        return 0

# for diagonal- left - bottom


def diag_left_bottom(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr+1
    tempc = cc-1
    while(tempr < tr and tempc >= 0):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bpos = tempr
            break
        tempr += 1
        tempc -= 1
    if bpos != -1:
        return abs(bpos-cr)-1
    else:
        return 0

# for diagonal- right - bottom


def diag_right_bottom(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr+1
    tempc = cc+1
    while(tempr < tr and tempc < tc):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bpos = tempr
            break
        tempr += 1
        tempc += 1
    if bpos != -1:
        return abs(cr-bpos)-1
    else:
        return 0


def get_move_value(state, player, row, column):
    tr = len(state)
    tc = len(state[0])
    flipped = 0
    flipped += diag_left_top(state, player, row, column) + \
        diag_right_top(state, player, row, column)
    flipped += diag_left_bottom(state, player, row, column) + \
        diag_right_bottom(state, player, row, column)
    flipped += vert_up(state, player, row, column) + \
        vert_dow(state, player, row, column)
    flipped += hor_right(state, player, row, column) + \
        hor_left(state, player, row, column)

    return flipped


"""
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
"""


def execute_move(state, player, row, column):
    # new_state=[]
    # new_state.clear()
    valid = get_move_value(state,player,row,column)
    if valid != 0:
        new_state = copy.deepcopy(state)
        new_state[row][column] = player
        cr = row
        cc = column
        new_state = vert_down(new_state, player, cr, cc)
        new_state = vert_upexec(new_state, player, cr, cc)
        new_state = hor_rightexec(new_state, player, cr, cc)
        new_state = hor_leftexec(new_state, player, cr, cc)
        new_state = diag_left_topexec(new_state, player, cr, cc)
        new_state = diag_right_topexec(new_state, player, cr, cc)
        new_state = diag_left_bottomexec(new_state, player, cr, cc)
        new_state = diag_right_bottomexec(new_state, player, cr, cc)
    # Your implementation goes here
        return new_state
    else:
        return state

# for vertical downwards


def vert_down(state, player, cr, cc):
    tr = len(state)

    tc = len(state[0])
    bpos = -1
    for i in range(cr+1, tr):
        if state[i][cc] == ' ':
            break
        if state[i][cc] == player:
            bpos = i
            break
    if bpos != -1:
        for i in range(bpos, cr, -1):
            state[i][cc] = player
    return state
# for vertical upwards


def vert_upexec(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    for i in range(cr-1, -1, -1):
        if state[i][cc] == ' ':
            break
        if state[i][cc] == player:
            bpos = i
            break
    if bpos != -1:
        for i in range(bpos, cr):
            state[i][cc] = player
    return state

# for horizontal right side


def hor_rightexec(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    for i in range(cc+1, tc):
        if state[cr][i] == ' ':
            break
        if state[cr][i] == player:
            bpos = i
            break
    if bpos != -1:
        for i in range(bpos, cc, -1):
            state[cr][i] = player
    return state

# for horizontal left side


def hor_leftexec(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    for i in range(cc-1, -1, -1):
        if state[cr][i] == ' ':
            break
        if state[cr][i] == player:
            bpos = i
            break
    if bpos != -1:
        for i in range(bpos, cc):
            state[cr][i] = player
    return state

# for diagonal- left - top


def diag_left_topexec(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr-1
    tempc = cc-1
    bposr = -1
    bposc = -1
    while(tempr >= 0 and tempc >= 0):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bposr = tempr
            bposc = tempc
            break
        tempr -= 1
        tempc -= 1
    if bposr != -1:
        while(bposr <= cr and bposc <= cc):
            state[bposr][bposc] = player
            bposc += 1
            bposr += 1
    return state

# for diagonal- right - top


def diag_right_topexec(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr-1
    tempc = cc+1
    bposr = -1
    bposc = -1
    while(tempr >= 0 and tempc < tc):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bposr = tempr
            bposc = tempc
            break
        tempr -= 1
        tempc += 1
    if bposr != -1:
        while(bposr <= cr and bposc >= cc):
            state[bposr][bposc] = player
            bposc -= 1
            bposr += 1
    return state

# for diagonal- left - bottom


def diag_left_bottomexec(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr+1
    tempc = cc-1
    bposr = -1
    bposc = -1
    while(tempr < tr and tempc >= 0):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bposr = tempr
            bposc = tempc
            break
        tempr += 1
        tempc -= 1
    if bposr != -1:
        while(bposr >= cr and bposc <= cc):
            state[bposr][bposc] = player
            bposc += 1
            bposr -= 1
    return state
# for diagonal- right - bottom


def diag_right_bottomexec(state, player, cr, cc):
    tr = len(state)
    tc = len(state[0])
    bpos = -1
    tempr = cr+1
    tempc = cc+1
    bposr = -1
    bposc = -1
    while(tempr < tr and tempc < tc):
        if state[tempr][tempc] == ' ':
            break
        if state[tempr][tempc] == player:
            bposr = tempr
            bposc = tempc
            break
        tempr += 1
        tempc += 1
    if bposr != -1:
        while(bposr >= cr and bposc >= cc):
            state[bposr][bposc] = player
            bposc -= 1
            bposr -= 1
    return state


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,
    return (4, 3)
"""


def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    for i in range(0, len(state)):
        for j in range(0, len(state)):
            if state[i][j] == 'B':
                blackpieces += 1
            elif state[i][j] == 'W':
                whitepieces += 1

    return (blackpieces, whitepieces)


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = False
    sp = 0
    for i in range(0, len(state)):
        if ' ' in state[i]:
            sp = 1
            break
    if sp == 0:
        terminal = True
        return terminal
    for i in range(0, len(state)):
        for j in range(0, len(state[0])):
            if state[i][j] == ' ':
                if get_move_value(state, 'B', i, j) != 0:
                    return False
                if get_move_value(state, 'W', i, j) != 0:
                    return False
    return True


"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""


d = {}
dist = dict()
branchNo = 1
distt = {}

move_dictionary = dict()
count_mm=0

def minimax(state, player):
    global count_mm
    getting_allPossiblemoves = list()
    getting_allPossiblemoves = getPossibleMoves(state, player)

    if(len(getting_allPossiblemoves) == 0):
        if is_terminal_state(state):
            count_mm+=1
            b, w = count_pieces(state)

            return (b-w, -1, -1)
        if player == 'W':
            player = 'B'
        else:
            player = 'W'

        getting_allPossiblemoves = getPossibleMoves(state, player)

    allChildNodes = dict()
    for i in getting_allPossiblemoves:
        rowc, columnc = i
        childNode = execute_move(state, player, rowc, columnc)
        allChildNodes[i] = childNode
    if(player == 'B'):
        v = -9999
        for move, child in allChildNodes.items():
            (eval, row, column) = minimax(child, 'W')
            if (eval > v):
                v = eval
                rowb, columnb = move
        return (v, rowb, columnb)
    else:
        v = 9999
        for move, child in allChildNodes.items():
            (eval, row, column) = minimax(child, 'B')
            if (eval < v):
                v = eval
                rowb, columnb = move

        return (v, rowb, columnb)


def getPossibleMoves(state, player):
    l = list()
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == ' ':
                val = get_move_value(state, player, i, j)
                if(val > 0):
                    l.append((i, j))
                else:
                    continue
    return l


"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""
move_sequence_minimax = list()


def full_minimax(state, player):
    v = minimax(state, player)[0]
    move_sequence_minimax.clear()
    while(1):
        if player == 'B':
            val, r, c = minimax(state, 'B')
        else:
            val, r, c = minimax(state, 'W')
        if len(getPossibleMoves(state, player)) == 0:
            if is_terminal_state(state):
                move_sequence_minimax.append((player, r, c))
                break
            else:
                if player == 'B':
                    player = 'W'
                else:
                    player = 'B'
                continue
        move_sequence_minimax.append((player, r, c))
        state = execute_move(state, player, r, c)
        if player == 'B':
            player = 'W'
        else:
            player = 'B'
    v = val
    print(move_sequence_minimax)

    return([v, move_sequence_minimax])


"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""
count_ab=0
count_terminal = 0
def minimax_ab(state, player, alpha=-10000000, beta=10000000):
    global count_terminal, count_ab
    allPossiblemoves = list()
    allPossiblemoves = getPossibleMoves(state, player)
    if(len(allPossiblemoves) == 0):
        if is_terminal_state(state):
            b, w = count_pieces(state)
            count_terminal += 1
            return (b-w, -1, -1)
        if player == 'W':
            player = 'B'
        else:
            player = 'W'

        allPossiblemoves = getPossibleMoves(state, player)

    allChildNodes = dict()
    for i in allPossiblemoves:
        rowc, columnc = i
        childNode = execute_move(state, player, rowc, columnc)
        allChildNodes[i] = childNode
    if(player == 'B'):
        v = -9999
        for move, child in allChildNodes.items():
            (eval, row, column) = minimax_ab(child, 'W', alpha, beta)

            if (eval > v):
                v = eval
                rowb, columnb = move
            if(alpha < eval):
                alpha = eval
            if(beta <= alpha):
                break
        return (v, rowb, columnb)
    else:
        v = 9999
        for move, child in allChildNodes.items():
            (eval, row, column) = minimax_ab(child, 'B', alpha, beta)
            if (eval < v):
                v = eval
                rowb, columnb = move
            if(beta > eval):
                beta = eval
            if(beta <= alpha):
                break
        return (v, rowb, columnb)


"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""
move_sequence_ab = list()


def full_minimax_ab(state, player):
    global count_terminal
    move_sequence_ab.clear()
    v = minimax_ab(state, player)[0]
    while(1):
        if player == 'B':
            val, r, c = minimax_ab(state, 'B')
        else:
            val, r, c = minimax_ab(state, 'W')
        if len(getPossibleMoves(state, player)) == 0:
            if is_terminal_state(state):
                move_sequence_ab.append((player, r, c))
                break
            else:
                if player == 'B':
                    player = 'W'
                else:
                    player = 'B'
                continue
        move_sequence_ab.append((player, r, c))

        state = execute_move(state, player, r, c)
        if player == 'B':
            player = 'W'
        else:
            player = 'B'
    v = val
    return([v, move_sequence_ab])
