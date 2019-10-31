import connectfour
import local_connect_four
import socket_handling

COLOR = {connectfour.RED:'Red', connectfour.YELLOW:'Yellow'}




def startup(game_state):

    user_input_host = 'circinus-32.ics.uci.edu' #change back to 'input('What is the host name: ')'
    user_input_port = 4444 # change back to int(input('What is the port number'))
    print("Connecting...")

    game_connection = socket_handling.connect(user_input_host,user_input_port)

    print(f"Successfully Connected to {user_input_host} at port {user_input_port}")

    first_line = 'I32CFSP_HELLO boo'
    game_connection.output.write(first_line + '\r\n')
    game_connection.output.flush()
    print(game_connection.input.readline())

    second_line = 'AI_GAME'
    game_connection.output.write(second_line + '\r\n')
    game_connection.output.flush()
    print(game_connection.input.readline())


    #Code to run the game and search for exceptions
    
    gameplay(game_state, game_connection)
    socket_handling.close(game_connection)





def user_input(game_state, game_connection) -> 'game_state':
    '''Takes user input and updates the game_state. Then sends the input to connected server. Returns the game_state.'''
    
    user_input = local_connect_four.user_input(game_state)
    game_state = local_connect_four.drop_or_pop_action(game_state, user_input)

    game_connection.output.write(user_input +'\r\n')
    game_connection.output.flush()

    return game_state


def server_input(game_state, game_connection) -> 'game_state':
    '''Reads input from the server, and updates game_state based on what is read. Returns the game_state.'''
    print(game_connection.input.readline())
    game_state = local_connect_four.drop_or_pop_action(game_state, game_connection.input.readline())
    print(game_connection.input.readline())

    return game_state

def gameplay(game_state, game_connection) -> None:
    '''Main gameplay funtion. Ends the game/breaks out of loop if an error is found. '''
    
    while True:
        try:
            if game_state.turn == connectfour.RED:
                local_connect_four.print_board(game_state)
                game_state = user_input(game_state, game_connection)
            elif game_state.turn == connectfour.YELLOW: 
                local_connect_four.print_board(game_state)
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
            local_connect_four.print_board(game_state)
            local_connect_four.who_won(game_state)
            break
             

         

if __name__ == '__main__':
    game_state = connectfour.new_game()
    startup(game_state)

