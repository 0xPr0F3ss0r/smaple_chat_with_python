import socket
import threading
import os


PORT = 7777
IPV4 = socket.gethostbyname(socket.gethostname())
def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024)
            if not message:
                break
            print(f": {message.decode('utf-8')}")
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_messages(sock):
    while True:
        os.system("color a")
        try:
            message = input("Enter message: ")
            if message == "exit":
                break
            elif message == "clear" or message == "cls":
                 clear_console(message)
            elif message ==  "color c":
                 os.system("color c")
            sock.send(message.encode('utf-8'))
        except Exception as e:
            print(f"Error sending message: {e}")
            break

def clear_console(message):
    if message == "clear":  # Windows
         os.system('clear')    
    
    os.system("cls")
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IPV4, PORT))

    # Start threads for receiving and sending messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket,)).start()

start_client()
