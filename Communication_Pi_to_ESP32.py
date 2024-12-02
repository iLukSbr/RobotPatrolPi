import serial
import time


#ser.reset_input_buffer()

# Configurar a porta serial
ser = serial.Serial('/dev/serial0', baudrate=115200, timeout=1)

while True:
    # Enviar dados
    ser.write(b'Hello ESP32!\n')
    print("Mensagem enviada para o ESP32")
    time.sleep(1)
    print("sleep 1")
    # Receber dados
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        print(f"Recebido do ESP32: {data}")

