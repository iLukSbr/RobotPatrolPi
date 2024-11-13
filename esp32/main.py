import machine
import time

# Configuração do pino do LED
led = machine.Pin(2, machine.Pin.OUT)

def blink_led():
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)

if __name__ == "__main__":
    while True:
        print("Hello, World!")
        blink_led()