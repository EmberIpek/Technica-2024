import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

segments = (7, 11, 29, 31, 12, 16, 38)
digits = (36, 32)
back = 35
forward = 37
binarys = (40, 22, 33, 15, 18)

# set up pins
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
    
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)
    
for binary in binarys:
    GPIO.setup(binary, GPIO.OUT)
    GPIO.output(binary, GPIO.LOW)

# pull up resistors required to accomodate for switch bounce
GPIO.setup(back, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(forward, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def toBaseTwo(num):
    # LED bar output
    for i in range(0, 5):
        if (num % 2 == 1):
            GPIO.output(binarys[i], GPIO.LOW)
        else:
            GPIO.output(binarys[i], GPIO.HIGH)
        num = num // 2

def number(num):
    # segments to light up according to input
    if(num == 0):
        GPIO.output(segments[0], GPIO.HIGH)
        GPIO.output(segments[1], GPIO.HIGH)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.LOW)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.HIGH)
        GPIO.output(segments[6], GPIO.HIGH)
    elif(num == 1):
        GPIO.output(segments[0], GPIO.LOW)
        GPIO.output(segments[1], GPIO.LOW)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.LOW)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.LOW)
        GPIO.output(segments[6], GPIO.LOW)
    elif(num == 2):
        GPIO.output(segments[0], GPIO.HIGH)
        GPIO.output(segments[1], GPIO.HIGH)
        GPIO.output(segments[2], GPIO.LOW)
        GPIO.output(segments[3], GPIO.HIGH)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.LOW)
        GPIO.output(segments[6], GPIO.HIGH)
    elif(num == 3):
        GPIO.output(segments[0], GPIO.LOW)
        GPIO.output(segments[1], GPIO.HIGH)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.HIGH)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.LOW)
        GPIO.output(segments[6], GPIO.HIGH)
    elif(num == 4):
        GPIO.output(segments[0], GPIO.LOW)
        GPIO.output(segments[1], GPIO.LOW)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.HIGH)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.HIGH)
        GPIO.output(segments[6], GPIO.LOW)
    elif(num == 5):
        GPIO.output(segments[0], GPIO.LOW)
        GPIO.output(segments[1], GPIO.HIGH)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.HIGH)
        GPIO.output(segments[4], GPIO.LOW)
        GPIO.output(segments[5], GPIO.HIGH)
        GPIO.output(segments[6], GPIO.HIGH)
    elif(num == 6):
        GPIO.output(segments[0], GPIO.HIGH)
        GPIO.output(segments[1], GPIO.HIGH)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.HIGH)
        GPIO.output(segments[4], GPIO.LOW)
        GPIO.output(segments[5], GPIO.HIGH)
        GPIO.output(segments[6], GPIO.HIGH)
    elif(num == 7):
        GPIO.output(segments[0], GPIO.LOW)
        GPIO.output(segments[1], GPIO.LOW)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.LOW)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.LOW)
        GPIO.output(segments[6], GPIO.HIGH)
    elif(num == 8):
        GPIO.output(segments[0], GPIO.HIGH)
        GPIO.output(segments[1], GPIO.HIGH)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.HIGH)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.HIGH)
        GPIO.output(segments[6], GPIO.HIGH)
    elif(num == 9):
        GPIO.output(segments[0], GPIO.LOW)
        GPIO.output(segments[1], GPIO.HIGH)
        GPIO.output(segments[2], GPIO.HIGH)
        GPIO.output(segments[3], GPIO.HIGH)
        GPIO.output(segments[4], GPIO.HIGH)
        GPIO.output(segments[5], GPIO.HIGH)
        GPIO.output(segments[6], GPIO.HIGH)
    else:
        GPIO.output(segments[0], GPIO.LOW)
        GPIO.output(segments[1], GPIO.LOW)
        GPIO.output(segments[2], GPIO.LOW)
        GPIO.output(segments[3], GPIO.LOW)
        GPIO.output(segments[4], GPIO.LOW)
        GPIO.output(segments[5], GPIO.LOW)
        GPIO.output(segments[6], GPIO.LOW)

def display(num):
    # display each digit on 7-segment display
    for _ in range(2):
        GPIO.output(digits[0], GPIO.LOW)
        number(num % 10)
        time.sleep(0.001)
        GPIO.output(digits[0], GPIO.HIGH)
        GPIO.output(digits[1], GPIO.LOW)
        number((num // 10) % 10)
        time.sleep(0.001)
        GPIO.output(digits[1], GPIO.HIGH)

try:
    i = 0
    resetted = False
    forwarded = False
    backed = False
    while True:
            
        # latch to avoid multiple inputs while holding down button
        forwarding = GPIO.input(forward) == 1
        backing = GPIO.input(back) == 1
        
        # check button conditions
        if((forwarding) and (backing)):
            i = 0
            forwarded = True
            backed = True
            continue
            
        if(forwarding and not forwarded):
            i += 1
        forwarded = forwarding
           
        if(backing and not backed and i > 0):
            i -= 1
        backed = backing
        
        if(i == 32):
            i = 0
        
        # output result onto 7-segment display and LED bar
        display(i)
        toBaseTwo(i)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
