import socket

def start_server():
    # Create a socket object using TCP/IP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port
    server_address = ('localhost', 6799)  # You can change the port number if needed
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is waiting for a connection...")
    
    # Accept a connection
    connection, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                print("Received:", data.decode())
            else:
                # If no data is received, break the loop
                print("No more data from", client_address)
                break
    finally:
        # Clean up the connection
        connection.close()
        print("Connection closed.")

if __name__ == '__main__':
    start_server()
