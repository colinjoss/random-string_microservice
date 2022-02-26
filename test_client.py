import socket

HOST = socket.gethostname()
PORT = 50005

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create client socket
client_socket.connect((HOST, PORT))                                 # Make connection with host socket
client_socket.send('12-110'.encode())                                  # Send GET request
res = client_socket.recv(400)                                       # Receive host response

print('Response:', res.decode())                                    # Display response

client_socket.close()                   # Close connection
