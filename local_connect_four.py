import connectfour
import shared_functions



COLOR = {connectfour.RED:'Red', connectfour.YELLOW:'Yellow'}





def gameplay(game_state):
    while True:
        try:
            shared_functions.print_board(game_state)
            _user_input = shared_functions.user_input(game_state)
            game_state = shared_functions.drop_or_pop_action(game_state, _user_input)
        except IndexError:
            print("INVALID")
            continue
        except connectfour.InvalidMoveError:
            shared_functions.print_board(game_state)
            continue
        except connectfour.GameOverError:
            print("Game is already over")
            break
        except ValueError:
            shared_functions.print_board(game_state)
            continue
        except AttributeError:
            print('INVALID')
            continue
        if connectfour.winner(game_state)==connectfour.RED or connectfour.winner(game_state) == connectfour.YELLOW:
            shared_functions.who_won(game_state)
            break

    print("End of game")


if __name__ == '__main__':

    gamestate = connectfour.new_game()
    gameplay(gamestate)

    

