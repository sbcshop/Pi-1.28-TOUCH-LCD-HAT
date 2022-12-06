#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import smbus
import time
import logging
import spidev as SPI
from lib import RoundLCD
from PIL import Image,ImageDraw,ImageFont

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

GPIO.setup(23,GPIO.OUT)
GPIO.output(23,GPIO.HIGH)

GPIO.setup(4, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(19, GPIO.IN)
Touch_int = 4 
GPIO.setup(Touch_int, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0

# colors
WHITE   = 0xFFFF
BLACK   = 0x0000
GRAY    = 0xF7DE
BLUE    = 0x001F
BLUE2   = 0x051F
RED     = 0xF800
PURPLE  = 0xF81F
GREEN   = 0x07E0
CYAN    = 0x7FFF
YELLOW  = 0xFFE0
DGREEN  = 0x07E0


PONT = 0x08
GESTURES = 0x80
TAP = 0x20
FLICK = 0x22
DOUBLE_TAP = 0x23
UP = 0x08
UPPER_RIGHT = 0x09
RIGHT = 0x0A
LOWER_RIGHT = 0x0B
DOWN = 0x0C
DOWN_LEFT = 0xEC
LOWER_LEFT= 0x0D
LEFT =0x0E
UPPER_LEFT =0x0F

bus = smbus.SMBus(1)
address = 0x46
DEVICE_ADDRESS = 0x46  

#logging.basicConfig(level=logging.DEBUG)

for device in range(128):

      try:
         bus.read_byte(0X46)
         bus.read_byte(device)
         print(hex(device))
         if device == address :
             #open(bus)
             
             print("touch device found")
         else :
             print("touch device not found")
             
      except: # exception if read_byte fails
         #print("No device not found")
         pass

Font1 = ImageFont.truetype("Font/Font02.ttf",45)
Font2 = ImageFont.truetype("Font/Font02.ttf",20)

def CTP_CheckBusy():
    val = bus.read_byte_data(DEVICE_ADDRESS,0x80)
    return val
def CTP_IdentifyCapSen():
   
    ctpCheck = CTP_CheckBusy()
    if ctpCheck == 192 :
        print("touch busy")
    ret = bus.write_byte_data(DEVICE_ADDRESS,0x20,0)
    if ret == 0:
        print("cmd_bufferindex falied")
    ctpCheck = CTP_CheckBusy()
    if ctpCheck == 192 :
        print("touch busy")
    data = bus.read_i2c_block_data(DEVICE_ADDRESS,0xA0,10)
    print(data)
    lst = [10,73,84,69,55,50,53,57,50,48]
    for i in range(10):
        if (data[i]) == lst[i] :
            print("match data")
            return 1
        else :
            print("data not matched")
            return 0
    

try:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    disp = RoundLCD.RoundLCD_HAT()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    

    image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")
    draw = ImageDraw.Draw(image1)
    #draw.arc((1,1,237,237),0, 360, fill =(0,0,255), width=9)
    im_r=image1.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(1)
    image = Image.open('pic/lcd_logo.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(2)

    image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
    draw2 = ImageDraw.Draw(image2)
    

    #draw2.arc((1,1,240,240),0, 360, fill =(26,246,136), width=9)
       
    #draw2.text((75, 90), "Hello !", font=Font1, fill = (255,255,255))
    #draw2.text((90, 138), "Welcome", font=Font2, fill = (255,255,255))
    im_r2=image2.rotate(0)
    disp.ShowImage(im_r2)
    ret = CTP_IdentifyCapSen()
    if ret == 1 :
        print("touch driver working fine")
    else :
        print("touch driver not working ")
    i =0
    while True:
        GPIO.wait_for_edge(Touch_int, GPIO.FALLING)
        
        i+=1
        print(i)
        if i == 7 :
            i =0;
            
        if i == 0:
            
            draw2.arc((1,1,240,240),0, 360, fill =(0,153,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 1:
            
            draw2.arc((1,1,240,240),0, 360, fill =(255,51,153), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 2:
            
            draw2.arc((1,1,240,240),0, 360, fill =(0,204,0), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 3:
            
            #draw2.arc((1,1,240,2407),0, 360, fill =(255,255,31), width=9)
            #im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 4:
            
            draw2.arc((1,1,240,240),0, 360, fill =(255,255,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)
       
        
       # bear = bus.read_i2c_block_data(address,128,1)
        #bus.read_byte(0X46)
        print(bus.read_byte_data(DEVICE_ADDRESS,0x80))
        #stat = bus.read_i2c_block_data(DEVICE_ADDRESS,0x05,10)
       # print(stat)
        stat = bus.read_i2c_block_data(DEVICE_ADDRESS,0xE0,11)
        print(stat)
        '''
        if stat[0] and PONT:
            
            x = ((stat[3] and 0x0F) << 8) + stat[2]
            print(x)
            y = ((stat[3] and 0xF0) << 4) + stat[4]
            print(y)
            draw2.text((x,y), "O", font=Font2, fill = (255,255,255))
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)
            '''
        if stat[0] and GESTURES:
            print("GESTURES")
            if stat[1] == TAP or stat[1] == DOUBLE_TAP:
                print("TAP")
                #draw2.text((x,y), "O", font=Font2, fill = (255,0,0))
                #im_r2=image2.rotate(0)
                #disp.ShowImage(im_r2)
            if stat[1] == FLICK :
                print("FLICK")
                if stat[10] == UP:
                    print("UP")
                if stat[10] == UPPER_RIGHT:
                    print("UPPER_RIGHT")
                if stat[10] == RIGHT:
                    print("RIGHT")
                    i+=1
                    print(i)
                    if i == 7 :
                        i =7;
                if stat[10] == LOWER_RIGHT:
                    print("LOWER_RIGHT")
                if stat[10] == DOWN:
                    print("DOWN")
                if stat[10] == DOWN_LEFT:
                    print("DOWN_LEFT")
                if stat[10] == LEFT:
                    print("LEFT")
                    i-=1
                    print(i)
                    if i <= 0 :
                        i =0;
                if stat[10] == UPPER_LEFT:
                    print("UPPER_LEFT")
        if i == 0:
            image2=Image.new("RGB", (disp.width, disp.height), (0,153,255))
            #draw2.arc((1,1,240,240),0, 360, fill =(0,153,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 1:
            image2=Image.new("RGB", (disp.width, disp.height), (255,51,153))
            #draw2.arc((1,1,240,240),0, 360, fill =(255,51,153), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 2:
            image2=Image.new("RGB", (disp.width, disp.height), (0,204,0))
            #draw2.arc((1,1,240,240),0, 360, fill =(0,204,0), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 3:
            image2=Image.new("RGB", (disp.width, disp.height), (255,255,31))
            #draw2.arc((1,1,240,240),0, 360, fill =(255,255,31), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)

        elif i == 4:
            image2=Image.new("RGB", (disp.width, disp.height), (10,255,10))
            #draw2.arc((1,1,240,240),0, 360, fill =(10,255,10), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)
        elif i == 5:
            image2=Image.new("RGB", (disp.width, disp.height), (255,25,255))
            #draw2.arc((1,1,240,240),0, 360, fill =(255,25,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)
        elif i == 6:
            image2=Image.new("RGB", (disp.width, disp.height), (255,25,25))
           # draw2.arc((1,1,240,240),0, 360, fill =(255,255,25), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)
        elif i == 7:
            image2=Image.new("RGB", (disp.width, disp.height), (25,25,255))
            #draw2.arc((1,1,240,240),0, 360, fill =(25,255,255), width=9)
            im_r2=image2.rotate(0)
            disp.ShowImage(im_r2)
      
        #print()
        #bearing = bearing3599()     #this returns the value to 1 decimal place in degrees. 
        #bear255 = bearing255()      #this returns the value as a byte between 0 and 255. 
        #print(bearing)
       # print(bear255)
        #time.sleep(1)

        
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()

