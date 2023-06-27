#!/usr/bin/python
import os
import sys 
import time
import spidev as SPI
sys.path.append("..")
from lib import Round_Touch
from PIL import Image,ImageDraw,ImageFont

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) 

GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(19, GPIO.IN)

Font1 = ImageFont.truetype("../Font/Font02.ttf",45)
Font2 = ImageFont.truetype("../Font/Font02.ttf",20)

try:
    disp = Round_Touch.lcd()
    disp.Init()
    disp.clear()
    image = Image.open('../pic/lcd_logo.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(2)

    image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
    draw2 = ImageDraw.Draw(image2)
    

    draw2.arc((1,1,240,240),0, 360, fill =(26,246,136), width=9)
       


    while True:

        if GPIO.input(6) == GPIO.LOW:
                                image = Image.open('../pic/img1.jpg')	
                                im_r2=image.rotate(0)
                                disp.ShowImage(im_r2)
                                print("RIGHT BUTTON")
        
        if GPIO.input(13) == GPIO.LOW:
                                
                                image = Image.open('../pic/img4.jpg')	
                                im_r2=image.rotate(0)
                                disp.ShowImage(im_r2)
                                print("DOWN BUTTON")

        if GPIO.input(26) == GPIO.LOW:
                                
                                image = Image.open('../pic/img5.jpg')	
                                im_r2=image.rotate(0)
                                disp.ShowImage(im_r2)
                                print("LEFT BUTTON")

        if GPIO.input(5) == GPIO.LOW:
                                
                                image = Image.open('../pic/img8.jpg')	
                                im_r2=image.rotate(0)
                                disp.ShowImage(im_r2)
                                print("UP BUTTON")

        if GPIO.input(19) == GPIO.LOW:
                                image = Image.open('../pic/img7.jpg')	
                                im_r2=image.rotate(0)
                                disp.ShowImage(im_r2)
                                print("CENTRE BUTTON")
                                  
except KeyboardInterrupt:
    disp.module_exit()
    exit()
