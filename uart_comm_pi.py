import serial, time

class UARTComm:
    # BAUD_RATE = 115200
    # TIMEOUT = 1  # em segundos (para pySerial)
    BAUD_RATE = 9600
    TIMEOUT = 5
    
    def __init__(self, port='/dev/serial0', baudrate=BAUD_RATE, timeout=TIMEOUT):
        try:
            self.uart = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
            self.timeout = timeout
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
        # try:
        #     message = self.uart.readline().decode('utf-8').strip()
        #     if message:
        #         print(f"Received serial message: {message}")
        #     return message
        # except Exception as e:
        #     print(f"Failed to read serial message: {e}")
        #     return None
        try:
            buffer = ""
            start_time = time.perf_counter()
            
            while True:
                if self.uart.any():
                    data = self.uart.read()
                    if data:
                        buffer += data.decode('utf-8')
                        if '\n' in buffer:
                            lines = buffer.split('\n')
                            for line in lines[:-1]:
                                line = line.strip()
                                print(f"Received: {line}")
                                return line
                            buffer = lines[-1]
                    start_time = time.perf_counter()  # Reset the timeout timer
                if time.perf_counter() - start_time > self.timeout:
                    if buffer:
                        print(f"Received partial message: {buffer.strip()}")
                        return None
                    buffer = ""  # Clear the buffer after timeout
                    start_time = time.perf_counter()  # Reset the timeout timer
                time.sleep_ms(100)
        except Exception as e:
            print(f"Failed to read message: {e}")
            return None