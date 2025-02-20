import RPi.GPIO as GPIO
from time import sleep
import serial
import time

ser = serial.Serial('/dev/serial0', baudrate=115200, timeout=1)

GPIO.setwarnings(False)

# Right Motor
in1 = 17
in2 = 27
en_a = 4
# Left Motor
in3 = 5
in4 = 6
en_b = 13

#Time to wait
WAIT = 3
RIGHTTURN = 0.4
LEFTTURN = 0.42
FORWARDSIDES = 0.4

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_b,GPIO.OUT)

q=GPIO.PWM(en_a,100)
p=GPIO.PWM(en_b,100)
p.start(30)
q.start(30)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)

# Wrap main content in a try block so we can  catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent the user seeing lots of unnecessary error messages.
try:
# Create Infinite loop to read user input
   obstacle = 0
   time.sleep(45) #Time for disconnecting cables and placing robot on ground for testing
   print('Start')
   while(obstacle == 0):
       
      #GPIO.output(in1,GPIO.HIGH)
      #GPIO.output(in2,GPIO.LOW)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)

      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)

      print("Forward")
      
      if ser.in_waiting > 0:
         data = ser.readline().decode('utf-8').strip()
         print(f"Recebido do ESP32: {data}")
         if data == '1':
             print('Data is 1')
             obstacle = 1
        
   while(obstacle == 1):
      # Get user Input
      #user_input = input()

      # To see users input
      # print(user_input)
      
      p.start(50) #Increases speed
      q.start(50)

      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
      
      time.sleep(WAIT)
         
      #GPIO.output(in1,GPIO.LOW)
      #GPIO.output(in2,GPIO.HIGH)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)
      print('First Right')
         
      time.sleep(RIGHTTURN)
         
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
         
      time.sleep(WAIT)
      
      #GPIO.output(in1,GPIO.HIGH)
      #GPIO.output(in2,GPIO.LOW)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)

      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)

      print("First Forward")
         
      time.sleep(FORWARDSIDES)
         
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
         
      time.sleep(WAIT)
         
      #GPIO.output(in1,GPIO.HIGH)
      #GPIO.output(in2,GPIO.LOW)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.HIGH)
      print('First Left')
         
      time.sleep(LEFTTURN)
         
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
         
      time.sleep(WAIT)
         
      #GPIO.output(in1,GPIO.HIGH)
      #GPIO.output(in2,GPIO.LOW)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)

      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)

      print("Second Forward")
         
      time.sleep(0.5)
         
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
         
      time.sleep(WAIT)
         
      #GPIO.output(in1,GPIO.HIGH)
      #GPIO.output(in2,GPIO.LOW)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.HIGH)
      print('Second Left')
         
      time.sleep(LEFTTURN)
         
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
         
      time.sleep(WAIT)
         
      #GPIO.output(in1,GPIO.HIGH)
      #GPIO.output(in2,GPIO.LOW)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.HIGH)

      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)

      print("Third Forward")
         
      time.sleep(FORWARDSIDES)
         
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
         
      time.sleep(WAIT)
         
      #GPIO.output(in1,GPIO.LOW)
      #GPIO.output(in2,GPIO.HIGH)
      
      #For the other robot, uncomment 2 lines above and comment the 2 below
      
      GPIO.output(in1,GPIO.HIGH)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.HIGH)
      GPIO.output(in3,GPIO.LOW)
      print('Second Right')
         
      time.sleep(RIGHTTURN)
         
      GPIO.output(in1,GPIO.LOW)
      GPIO.output(in2,GPIO.LOW)

      GPIO.output(in4,GPIO.LOW)
      GPIO.output(in3,GPIO.LOW)
         
      time.sleep(WAIT)
      obstacle = 0
         
   GPIO.output(in1,GPIO.LOW)
   GPIO.output(in2,GPIO.LOW)

   GPIO.output(in4,GPIO.LOW)
   GPIO.output(in3,GPIO.LOW)

   print('Finish')
# If user press CTRL-C
except KeyboardInterrupt:
  # Reset GPIO settings
  GPIO.cleanup()
  print("GPIO Clean up")


