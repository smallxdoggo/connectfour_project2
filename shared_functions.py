import connectfour

COLOR = {connectfour.RED:'Red', connectfour.YELLOW:'Yellow'}

def print_board(gamestate):
    ui = ' 1  2  3  4  5  6  7\n'

    for column in range(connectfour.BOARD_ROWS):
        for row in range(connectfour.BOARD_COLUMNS):
                
            if gamestate.board[row][column] == 1:
                ui += ' R '
            elif gamestate.board[row][column] == 2:
                ui += ' Y '
            elif gamestate.board[row][column] == 0:
                ui += ' . '

            if row == connectfour.BOARD_ROWS:
                ui += '\n'    
                
    print(ui)

def user_input(game_state):
    while True:
        input_pop_or_drop = input(f" {COLOR[game_state.turn]} Pop or Drop (SPACE) Column(1-7) Ex. POP(SPACE)3: ")
        uppercase = input_pop_or_drop.upper()
        uppercase_spliter = uppercase.split()
        if uppercase_spliter[0] != 'DROP' and uppercase_spliter[0] !='POP':
            continue
        return uppercase
