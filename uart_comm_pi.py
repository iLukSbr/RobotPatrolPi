import serial, time

class UARTComm:
    # BAUD_RATE = 115200
    # TIMEOUT = 1  # em segundos (para pySerial)
    BAUD_RATE = 9600
    TIMEOUT = 5.0
    
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
            print(f"Sent UART message: {message}")
        except Exception as e:
            print(f"Failed to send UART message: {e}")

    def read_serial(self):
        # try:
        #     message = self.uart.readline().decode('utf-8').strip()
        #     if message:
        #         print(f"Received UART message: {message}")
        #     return message
        # except Exception as e:
        #     print(f"Failed to read UART message: {e}")
        #     return None
        try:
            buffer = ""
            start_time = time.perf_counter()
            
            while True:
                if self.uart.in_waiting:
                    data = self.uart.read(self.uart.in_waiting).decode('utf-8')
                    buffer += data
                    # print(f"Buffer: {buffer}")  # Debug: print buffer content
                    if '\n' in buffer:
                        lines = buffer.split('\n')
                        for line in lines[:-1]:
                            line = line.strip()
                            print(f"Received UART message: {line}")
                            return line
                        buffer = lines[-1]
                    start_time = time.perf_counter()  # Reset the timeout timer
                if time.perf_counter() - start_time > self.timeout:
                    print("Timeout reached without receiving a complete UART message.")
                    return None
                time.sleep(0.1)
        except Exception as e:
            print(f"Failed to read UART message: {e}")
            return None