import socket

def start_server():
    host = '127.0.0.1'  # localhost for testing; use IP for real network
    port = 12345

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started on {host}:{port}. Waiting for client to connect...")
    conn, addr = server_socket.accept()
    print(f"Client connected from {addr}.")

    while True:
        # Server sends message
        message = input("You: ")
        conn.send(message.encode())
        if message.lower() == "exit":
            print("Chat ended.")
            break

        # Server receives message
        client_msg = conn.recv(1024).decode()
        if client_msg.lower() == "exit":
            print("Client has left the chat.")
            break
        print("Client:", client_msg)

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
