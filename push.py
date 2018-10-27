# Use Raspberry Pi to control Servo Motor motion
# Tutorial URL: http://osoyoo.com/?p=937

import RPi.GPIO as GPIO
import time

def celebrate(magnitude=1):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    pin = 7

    # 2 is the most clockwise position
    # 8 is the middle
    # 12 is the most counterclockwise position

    start = 11
    change = 8

    GPIO.setup(pin, GPIO.OUT)

    print('Made PWM object on pin', pin, 'at 50Hz')
    Servo = GPIO.PWM(pin, 50)

    print('Starting pwm with a duty cycle of', start)
    Servo.start(start)

    time.sleep(0.5)

    print('Changing duty cycle to', change)
    Servo.ChangeDutyCycle(change)

    time.sleep(0.3)

    print('Returning to start duty cycle', start)
    Servo.ChangeDutyCycle(start)

    # min sleep time here should be 3
    # max sleep time here should be 10
    if magnitude < 1:
        magnitude = 1
    elif magnitude > 8:
        magnitude = 8
    print('Celebrating for', 2+magnitude, 'seconds!')
    time.sleep(2 + magnitude)

    print('Changing duty cycle to', change)
    Servo.ChangeDutyCycle(change)

    time.sleep(0.3)

    print('Returning to start duty cycle', start)
    Servo.ChangeDutyCycle(start)

    time.sleep(1)

    print('Done.')

    print('Stopping pwm')
    Servo.stop()

    print('Cleaning up')
    GPIO.cleanup()
