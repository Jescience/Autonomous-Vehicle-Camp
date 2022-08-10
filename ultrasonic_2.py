import RPi.GPIO as GPIO
import time

GPIO.setmode(GPI.BCM)
GPIO.setwarnings(False)

trig = 23
echo = 24
GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)

while True:
  GPIO.output(trig, True)
  time.sleep(0.00001) # 10 microseconds
  GPIO.output(trig, False)
  while GPIO.input(echo) == 0:
    pass
  start = time.time()
  while GPIO.input(echo) == 1:
    pass
  end = time.time()
  distance = ((end - start) * 34300) / 2
  print("distance:", distance, "cm")
  time.sleep(1)
  
  if distance < 20:
    print("LED on")
    GPIO.output(14, GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(14, GPIO.LOW)
