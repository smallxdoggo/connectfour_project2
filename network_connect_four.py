import connectfour
import socket_handling
import shared_functions



def startup() -> ('game_state', 'game_connection'):
    '''Startup game by connection to host and port. Handle username input. Return the initial game_state and game_connection.'''

    game_state = connectfour.new_game()
    
    user_input_host = 'circinus-32.ics.uci.edu' #change back to 'input('What is the host name: ')'
    user_input_port = 4444 # change back to int(input('What is the port number'))
    print("Connecting...")

    game_connection = socket_handling.connect(user_input_host,user_input_port)

    print(f"Successfully Connected to {user_input_host} at port {user_input_port}")

    first_line = 'I32CFSP_HELLO boo'
    write_and_flush(first_line, game_connection)
    print(game_connection.input.readline())

    second_line = 'AI_GAME'
    write_and_flush(second_line, game_connection)
    print(game_connection.input.readline())

    return game_state, game_connection
    

def write_and_flush(_input, game_connection) -> None:
    game_connection.output.write(_input + '\r\n')
    game_connection.output.flush()
    


def user_input(game_state, game_connection) -> 'game_state':
    '''Takes user input and updates the game_state. Then sends the input to connected server. Returns the game_state.'''
    
    user_input = shared_functions.user_input(game_state)
    game_state = shared_functions.drop_or_pop_action(game_state, user_input)

    write_and_flush(user_input, game_connection)

    return game_state


def server_input(game_state, game_connection) -> 'game_state':
    '''Reads input from the server, and updates game_state based on what is read. Returns the game_state.'''
    print(game_connection.input.readline())
    game_state = shared_functions.drop_or_pop_action(game_state, game_connection.input.readline())
    print(game_connection.input.readline())

    return game_state


def gameplay(game_state, game_connection) -> None:
    '''Main gameplay funtion. Ends the game/breaks out of loop if an error is found. '''
    
    while True:
        try:
            if game_state.turn == connectfour.RED:
                shared_functions.print_board(game_state)
                game_state = user_input(game_state, game_connection)
            elif game_state.turn == connectfour.YELLOW: 
                shared_functions.print_board(game_state)
                game_state = server_input(game_state, game_connection)

        except IndexError:   
            print('Game has ended with no winner')
            break
        except connectfour.InvalidMoveError:
            print('Game has ended with no winner')
            break
        except connectfour.GameOverError:
            print("Game is already over")
            break
        except ValueError:
            print('Game has ended with no winner')
            break
        except AttributeError:
            print('Game has ended with no winner')
            break

        if connectfour.winner(game_state)==connectfour.RED or connectfour.winner(game_state) == connectfour.YELLOW:
            shared_functions.print_board(game_state)
            shared_functions.who_won(game_state)
            break

    socket_handling.close(game_connection)
        
             

         

if __name__ == '__main__':   
    startup = startup()
    gameplay(startup[0], startup[1])

