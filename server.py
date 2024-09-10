import socket  as sock
import threading
import os
import errno
import time
s  = sock.socket(sock.AF_INET,sock.SOCK_STREAM)

PORT = 7777
SERVER  = '0.0.0.0'
#ADDR  = (PORT,SERVER)
s.bind((SERVER,PORT))

s.listen()
print(f"########### SERVER [{SERVER}] LISTEN to [{PORT}]")
clients = []


def handle_client(client_socket,addr):
    connect = True
    while connect:
        os.system("color a")
        try: 
            data = client_socket.recv(1024)
            data_decode = data.decode("utf-8")
            if not data:
                break
            else:
              Bradcast_message(client_socket,data)
        except Exception as e:
                if isinstance(e, OSError) and e.errno == errno.WSAECONNRESET: 
                     connect = False   
                     clien_add = b'addr'
                     Bradcast_message(client_socket ,"disconnected")
                     #print(f"Client {addr} disconnected from the server (WinError 10054).")
                     time.sleep(3)
                else:
                    print(f"ERROR: {e}")
                    connect = False  
                    time.sleep(5)

                


def get_client_address(client_socket):
    for sock, addr in clients:
        if sock == client_socket:
            return addr
        #return ("Unknown", "Unknown")

def Bradcast_message(client_socket, data):
    # Get the remote client's address (instead of local address)
    client_addr = client_socket.getpeername()  # Get remote client's address (IP and port)
    
    # Create the message to broadcast
    addr_str = f"{client_addr[0]}:{client_addr[1]}"  # IP:Port format

    if data == "disconnected":
        message = f"Client {addr_str} disconnected from the server."
    else:
        message = f"FROM {addr_str}: {data.decode('utf-8')}"  # Decode data only here
    
    message_encoded = message.encode("utf-8")
    
    # Broadcast to all clients except the sender
    for client in clients:
        if client != client_socket:
            try:
                client.send(message_encoded)
            except:
                clients.remove(client)
                client.close()

def start():
    while True:
        client_socket ,addr = s.accept()
        print("NEW CONNECTION FROM ",client_socket)
        clients.append(client_socket)
        thread = threading.Thread(target= handle_client,args= (client_socket,addr))
        thread.start()




start()