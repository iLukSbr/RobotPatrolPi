import serial

class UARTComm:
    BAUD_RATE = 115200
    TIMEOUT = 1  # em segundos (para pySerial)

    def __init__(self, port='/dev/serial0', baudrate=BAUD_RATE, timeout=TIMEOUT):
        try:
            self.uart = serial.Serial(port, baudrate, timeout=timeout)
            print(f"UART initialized on port {port} with baudrate {baudrate}")
        except Exception as e:
            print(f"Failed to initialize UART: {e}")

    def send_message(self, message):
        try:
            self.uart.write((message + '\n').encode('utf-8'))
            print(f"Sent message: {message}")
        except Exception as e:
            print(f"Failed to send message: {e}")

    def read_serial(self):
        try:
            message = self.uart.readline().decode('utf-8').strip()
            if message:
                print(f"Received serial message: {message}")
            return message
        except Exception as e:
            print(f"Failed to read serial message: {e}")
            return None