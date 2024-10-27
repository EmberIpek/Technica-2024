import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# segments = (7, 11, 13, 29, 31, 12, 16, 38)
segments = (7, 11, 29, 31, 12, 16, 38)
digits = (36, 32)
# reset = 33
back = 35
forward = 37
binarys = (40, 22, 33, 15, 18)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
    
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)
    
for binary in binarys:
    GPIO.setup(binary, GPIO.OUT)
    GPIO.output(binary, GPIO.LOW)
    
# GPIO.setup(reset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(back, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(forward, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
# num = {' ':(0,0,0,0,0,0,0),
#     '0':(1,1,1,1,1,1,0),
#     '1':(0,1,1,0,0,0,0),
#     '2':(1,1,0,1,1,0,1),
#     '3':(1,1,1,1,0,0,1),
#     '4':(0,1,1,0,0,1,1),
#     '5':(1,0,1,1,0,1,1),
#     '6':(1,0,1,1,1,1,1),
#     '7':(1,1,1,0,0,0,0),
#     '8':(1,1,1,1,1,1,1),
#     '9':(1,1,1,1,0,1,1)}

def toBaseTwo(num):
    
    for i in range(0, 5):
        if (num % 2 == 1):
            GPIO.output(binarys[i], GPIO.LOW)
        else:
            GPIO.output(binarys[i], GPIO.HIGH)
        num = num // 2

def number(num):
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
    #for digits in digit:
    for _ in range(2):
        GPIO.output(digits[0], GPIO.LOW)
        number(num % 10)
        time.sleep(0.001)
        GPIO.output(digits[0], GPIO.HIGH)
        GPIO.output(digits[1], GPIO.LOW)
        number((num // 10) % 10)
        time.sleep(0.001)
        GPIO.output(digits[1], GPIO.HIGH)
        # GPIO.output(digits[2], GPIO.LOW)
        # number((d // 100) % 10)
        # time.sleep(0.001)
        # GPIO.output(digits[2], GPIO.HIGH)
        # GPIO.output(digits[3], GPIO.LOW)
        # number((d // 1000) % 10)
        # time.sleep(0.001)
        # GPIO.output(digits[3], GPIO.HIGH)

try:
    i = 0
    resetted = False
    forwarded = False
    backed = False
    while True:
        # GPIO.output(digits[0], GPIO.LOW)
        # GPIO.output(digits[1], GPIO.LOW)
        # GPIO.output(digits[2], GPIO.LOW)
        # GPIO.output(digits[3], GPIO.LOW)
        # GPIO.output(segments[0], GPIO.LOW)
        # GPIO.output(segments[2], GPIO.HIGH)
        
        # for i in range(0, 10000):
            # numbers(i)
            #for _ in range(200):
            
            forwarding = GPIO.input(forward) == 1
            backing = GPIO.input(back) == 1
            
            if((forwarding) and (backing)):
                i = 0
                forwarded = True
                backed = True
                continue
            #resetted = resetting
            
            if(forwarding and not forwarded):
                i += 1
            forwarded = forwarding
                
            if(backing and not backed and i > 0):
                i -= 1
            backed = backing
            
            if(i == 32):
                i = 0
            
            display(i)
            toBaseTwo(i)
            # print(GPIO.input(reset))
            
            # if(num[i] == 0):
            #     GPIO.output(segments[i], GPIO.LOW)
            # elif(num[i] == 1):
            #     GPIO.output(segments[i], GPIO.HIGH)

        # for segment in segments:
        #     GPIO.output(num)
        # GPIO.output(7, GPIO.HIGH)
        # time.sleep(5)
        # GPIO.output(digits[1], 0)
        # GPIO.output(digits[2], 0)
        # for digit in range(4):
        #     for loop in range(0,7):
        #         GPIO.output(digits[digit], 0)
        #         GPIO.output(segments, num['8'[digit]])
        #         time.sleep(1)
        #         GPIO.output(digits[digit], 1)
        #         GPIO.output(segments, num['8'[digit]])
        #         time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    
