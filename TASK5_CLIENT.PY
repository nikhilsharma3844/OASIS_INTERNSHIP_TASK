import socket

def start_client():
    host = '127.0.0.1'  # server IP
    port = 12345

    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server. You can start chatting. Type 'exit' to quit.")

    while True:
        # Client receives message
        server_msg = client_socket.recv(1024).decode()
        if server_msg.lower() == "exit":
            print("Server has ended the chat.")
            break
        print("Server:", server_msg)

        # Client sends message
        message = input("You: ")
        client_socket.send(message.encode())
        if message.lower() == "exit":
            print("Chat ended.")
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
