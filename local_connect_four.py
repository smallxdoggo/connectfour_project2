import connectfour
import network_connect_four


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


def drop_or_pop_action(game_state,user_input):

    player_input_spliter = user_input.split()
    player_option = player_input_spliter[0].upper()
    player_column = int(player_input_spliter[1])-1

    if player_option == 'DROP':
        game_state = connectfour.drop(game_state, player_column)

        return game_state
    elif player_option == 'POP':
        game_state = connectfour.pop(game_state, player_column)

        return game_state



def who_won(game_state):
    if connectfour.winner(game_state) == connectfour.RED:
        print("Red is the winner")


    elif connectfour.winner(game_state) == connectfour.YELLOW:
        print("Yellow is the winner")





def gametest(game_state):

    print_board(game_state)
    game_on = True
    no_winner = True

    while game_on:
        while no_winner:
            try:
                user_type_input = user_input(game_state)
                game_state = drop_or_pop_action(game_state,user_type_input)
            except IndexError:
                print("INVALID")
                continue
            except connectfour.InvalidMoveError:
                print_board(game_state)
                continue
            except connectfour.GameOverError:
                print("Game is already over")
                no_winner = False
                game_on = False
                break
            except ValueError:
                print_board(game_state)
                continue
            except AttributeError:
                print('INVALID')
                continue
            if connectfour.winner(game_state)==connectfour.RED or connectfour.winner(game_state) == connectfour.YELLOW:
                who_won(game_state)
                no_winner = False
                game_on = False
                break
        if not game_on:
            break

    print("End of game")


if __name__ == '__main__':

    gamestate = connectfour.new_game()
    gametest(gamestate)

    

