# Keylogger

The uploaded Python code consists of two files: ClientKeylog.py and ServerKeylog.py. Here's a breakdown of what they do and how to use them:

ClientKeylog.py:

-This script is designed to capture keystrokes from the user's keyboard using the pynput library.

-It connects to a server via a socket (TCP/IP) and sends the captured keystrokes to the server.

The script works as follows:

-Key Listener: It listens for key presses and releases on the local machine using pynput.keyboard.Listener.

-Keystroke Handling: Each time a key is pressed, it sends the key data to a predefined server.

-Escape Key: If the escape key is pressed, the script will stop listening and close the socket connection.

ServerKeylog.py:

- This script is the server-side component that listens for incoming connections from the client (the ClientKeylog.py).
It works as follows:

--Socket Setup: The server listens on port 6799 for an incoming connection.
--Receiving Data: Once a connection is made, the server continuously receives data (keystrokes) from the client.
--Data Output: The server prints the received keystrokes to the console. If no data is received, it breaks the connection.

Directions for Use:


Prerequisites:

-Ensure both the ClientKeylog.py and ServerKeylog.py files are on the same network (or on the same machine if running locally).

-Make sure the pynput library is installed. You can install it via pip:

pip install pynput

Run the Server:

-Start the server by running the ServerKeylog.py file on the machine that will receive the keystrokes. You can do this by navigating to the directory where the file is located and running:
python ServerKeylog.py

-The server will wait for a connection and will display the message Server is waiting for a connection....

Run the Client:

-Start the client by running the ClientKeylog.py file on the machine that will capture the keystrokes. Run the following command:

python ClientKeylog.py

-The client will start capturing keystrokes, and it will send them to the server.

Stop the Client:

-To stop the client from capturing keystrokes, press the Escape key. This will close the connection to the server and stop the keystroke capturing process.
Security Warning:
