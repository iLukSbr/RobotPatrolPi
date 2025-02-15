from uart_comm_pi import UARTComm
import socket
import time

HOST = ''  # Listen on all available interfaces
PORT = 12345  # Port to listen on

UARTComm_instance = UARTComm()

while True:
    try:
        #parts = message.split(",")

        #co2 = parts[0]
        #temperature = parts[1]
        #humidity = parts[2]
        #nh3 = parts[3]
        #flame = parts[4]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            print(f"Server listening on port {PORT}")
    
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    # Send data periodically
                    message = UARTComm_instance.read_serial()
                    if message is not None:
                        conn.sendall(message.encode())
                        print(f"Sent: {message}")
            
                    time.sleep(1)  # Wait 1 second before sending the next message

    except Exception as e:
        print(f"Failed to get sensor data: {e}")