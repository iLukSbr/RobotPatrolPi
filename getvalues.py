from uart_comm_pi import UARTComm

UARTComm_instance = UARTComm()

while True:
    try:

        message = UARTComm_instance.read_serial()

        parts = message.split(",")

        co2 = parts[0]
        temperature = parts[1]
        humidity = parts[2]
        nh3 = parts[3]
        flame = parts[4]

    except Exception as e:
        print(f"Failed to process or get sensor data: {e}")
