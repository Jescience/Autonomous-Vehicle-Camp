GPIO.setup(10, GPIO.OUT)

if distance < 20:
  print("LED on")
  GPIO.output(18, GPIO.HIGH)
  time.sleep(1)
  print("LED off")
  GPIO.output(18, GPIO.LOW)
