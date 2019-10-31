import socket
from collections import namedtuple

GameConnection = namedtuple('GameConnection',['socket','input','output'])

def connect(host: str,port: int):

    game_socket = socket.socket()
    game_socket_tuple =(host,port)

    game_socket.connect(game_socket_tuple)

    game_input = game_socket.makefile('r')
    game_output = game_socket.makefile('w')
    return GameConnection(socket = game_socket,input = game_input,output = game_output)

def close(game_connection):

    game_connection.input.close()
    game_connection.output.close()
    game_connection.socket.close()
