import random as rd
import math
import socket


LOWERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIALS = '!@#$%^&*'


def generate_random_string(length, upper, number, special):
    chars = ''
    chars += LOWERS
    if upper:
        chars += UPPERS
    if number:
        chars += NUMBERS
    if special:
        chars += SPECIALS

    password = ''
    for i in range(0, length):
        password += chars[math.floor(rd.random() * len(chars))]

    return password


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # Create server socket
server_socket.bind((socket.gethostname(), 50005))                               # Bind socket to localhost
server_socket.listen(5)                                               # Listen for requests
print(f"Connected by ('{socket.gethostname()}', 50005)\n")

while True:
    client_connection, client_address = server_socket.accept()      # Get client connection
    req = client_connection.recv(1024).decode()                     # Get the client request

    print('Received:', req, '\n')                          # Display request

    if len(req) > 3:
        data = 'ERROR'
    else:
        data = req.split('')

    print('Sending >>>>>>>>>>')

    DATA = generate_random_string(length, upper, number, special)

    print('<<<<<<<<<<')
    client_connection.sendall(DATA.encode())         # Send data to client
    client_connection.close()                        # Close connection

    server_socket.close()                            # Close socket
