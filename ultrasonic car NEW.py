import RPi.GPIO as GPIO   # library that identifies the pins on the raspberry pi               
import time                #library that identifies time 

GPIO.setwarnings(False)  # Disables warnings related to GPIO to prevent unnecessary messages
GPIO.setmode(GPIO.BCM)  # Sets the GPIO pin numbering mode to BCM (Broadcom SOC channel numbering, so it matches the label)

TRIG = 17    #pin number on raspberry pi that trig on the ultrasonic sensor is connected to
ECHO = 27    #pin number on raspberry pi that echo on the ultrasonic sensor is connected to

in1=16   #pin number on raspberry pi that motor controller in1 is connected to
in2=12   #pin number on raspberry pi that motor controller in2 is connected to
in3=21   #pin number on raspberry pi that motor controller in3 is connected to
in4=5   #pin number on raspberry pi that motor controller in4 is connected to

GPIO.setup(TRIG,GPIO.OUT)  #indicating that trig is an output                
GPIO.setup(ECHO,GPIO.IN)    #indicating that echo is an input

GPIO.setup(in1,GPIO.OUT)   #indicating that in1 is an output
GPIO.setup(in2,GPIO.OUT)   #indicating that in2 is an output
GPIO.setup(in3,GPIO.OUT)   #indicating that in3 is an output
GPIO.setup(in4,GPIO.OUT)   #indicating that in4 is an output

def stop():               #define what stop means
   print ("stop")         #print word stop on computer screen
   GPIO.output(in1, 0)   # no power going to in1
   GPIO.output(in2, 0)   # no power going to in2
   GPIO.output(in3, 0)   # no power going to in3
   GPIO.output(in4, 0)   # no power going to in4
def forward():            #define what forward means
   GPIO.output(in1, 1)   #power going to in1
   GPIO.output(in2, 0)   #no power going to in2
   GPIO.output(in3, 1)   #power going to in3
   GPIO.output(in4, 0)   #no power going to in4
   print ("Forward")     # print word forward on computer screen
def back():               #define what back means
   GPIO.output(in1, 0)   #no power going to in1
   GPIO.output(in2, 1)   #power going to in2
   GPIO.output(in3, 0)   #no power going to in3
   GPIO.output(in4, 1)   #power going to in4
   print ("back")      #print word back on computer screen
def left():            #define what left means
   GPIO.output(in1, 0)   #no power going to in1
   GPIO.output(in2, 0)   #no power going to in2
   GPIO.output(in3, 1)   #power going to in3
   GPIO.output(in4, 0)   #no power going to in4
   print ("left")         #print word left on computer screen
def right():            #define what right means
   GPIO.output(in1, 1)   #power going to in1
   GPIO.output(in2, 0)   #no power going to in2
   GPIO.output(in3, 0)   #no power going to in3
   GPIO.output(in4, 0)   #no power going to in4
   print ("right")      #print word right on computer screen

stop()  # Calls the stop() function, likely to stop any movement initially
count = 0  # Initializes a counter variable to keep track of some event occurrences

while True:  # Infinite loop to continuously measure distance and take actions
    GPIO.output(TRIG, True)  # Sends a short pulse from the trigger pin
    time.sleep(0.00001)  # Waits for 10 microseconds (required for ultrasonic sensor)
    GPIO.output(TRIG, False)  # Turns off the trigger signal

    while GPIO.input(ECHO) == 0:  # Waits for the echo pin to receive the signal
        pass  # Does nothing, just waits

    start = time.time()  # Records the time when the echo signal is received

    while GPIO.input(ECHO) == 1:  # Waits for the echo signal to go low again
        pass  # Does nothing, just waits

    end = time.time()  # Records the time when the echo signal stops

    distance = ((end - start) * 34300) / 2  # Calculates the distance based on time delay
    print("distance:", distance, "cm")  # Prints the measured distance
    time.sleep(1)  # Waits for 1 second before the next measurement

    flag = 0  # Resets flag before checking distance condition

    if distance < 15:  # If an object is detected within 15 cm
        count = count + 1  # Increments the count
        stop()  # Calls the stop() function to halt movement
        time.sleep(1)  # Waits for 1 second
        back()  # Calls the back() function to move backward
        time.sleep(1.5)  # Moves backward for 1.5 seconds

        if (count % 3 == 1) & (flag == 0):  # If count is 1 modulo 3 and flag is 0
            right()  # Calls the right() function to turn right
            flag = 1  # Sets the flag to 1
        else:  
            left()  # Calls the left() function to turn left
            flag = 0  # Resets the flag to 0

        time.sleep(1.5)  # Waits for 1.5 seconds after turning
        stop()  # Calls stop() again to halt movement
        time.sleep(1)  # Waits for another second
    else:  
        forward()  # Calls the forward() function to keep moving forward
        flag = 0  # Resets the flag to 0
