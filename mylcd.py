import time
from Adafruit_CharLCD import Adafruit_CharLCD

#rs phys26 bcm7, en phys19 bcm10, d4 phys15 bcm22, d5 phys8 bcm14, d6 phys24 bcm8, d7 phys11 bcm17

def init():
    #lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=8, d6=5, d7=11, cols=16, lines=2)
    lcd =  Adafruit_CharLCD(rs=7, en=10, d4=22, d5=14, d6=8, d7=17, cols=16, lines=2)
    return lcd

def display(message):
    lcd = init()
    lcd.clear()

    lcd.message(message)
    time.sleep(3)
    
    for x in range(0,16):
        lcd.move_right()
        time.sleep(0.1)
    
    time.sleep(3)
        
    for x in range(0,16):
        lcd.move_left()
        time.sleep(0.1)
        
