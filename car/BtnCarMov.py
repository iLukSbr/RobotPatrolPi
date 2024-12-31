import socket
import time
from threading import Thread
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# Right Motor
in1 = 17
in2 = 27
en_a = 4
# Left Motor
in3 = 5
in4 = 6
en_b = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_b,GPIO.OUT)

q=GPIO.PWM(en_a,100)
p=GPIO.PWM(en_b,100)
p.start(0)
q.start(0)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)

HOST = ''
PORT = 12345

p.ChangeDutyCycle(20)
q.ChangeDutyCycle(20)

button_state = None

def send_data_periodically(conn):
    while True:
        try:
            message = "1100,25,40,160,1"
            if button_state is not None:
                message += f",{button_state}"
            conn.sendall(message.encode())
            print(f"Sent: {message}")
            time.sleep(1)
        except (BrokenPipeError, ConnectionResetError):
            print("Cliente desconectado. Aguardando reconexao...")
            break

def receive_button_input(conn):
    global button_state
    while True:
        try:
            data = conn.recv(1024)
            if data:
                button_state = data.decode('utf-8').strip()
                print(f"Received button state: {button_state}")
                if button_state == "1":
                    GPIO.output(in1,GPIO.HIGH)
                    GPIO.output(in2,GPIO.LOW)

                    GPIO.output(in4,GPIO.HIGH)
                    GPIO.output(in3,GPIO.LOW)

                    print("Forward")
                    
                elif button_state == "0":
                    GPIO.output(in1,GPIO.LOW)
                    GPIO.output(in2,GPIO.LOW)

                    GPIO.output(in4,GPIO.LOW)
                    GPIO.output(in3,GPIO.LOW)
                    print('Stop')
                    
        except (BrokenPipeError, ConnectionResetError):
            print("Cliente desconectado. Aguardando reconexao...")
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Servidor ouvindo na porta {PORT}...")

        conn, addr = server_socket.accept()
        print(f"Conexao estabelecida com {addr}")

        Thread(target=send_data_periodically, args=(conn,), daemon=True).start()
        Thread(target=receive_button_input, args=(conn,), daemon=True).start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Servidor encerrado.")

if __name__ == "__main__":
    main()



