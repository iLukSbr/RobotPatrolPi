import socket
import time

HOST = ''  # Listen on all available interfaces
PORT = 12345  # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on port {PORT}")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Send data periodically
            
            message = "100,25,40,160,Detectada"
            conn.sendall(message.encode())
            print(f"Sent: {message}")
            
            time.sleep(1)  # Wait 1 second before sending the next message

