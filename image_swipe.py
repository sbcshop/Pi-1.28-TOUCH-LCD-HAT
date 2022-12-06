#!/usr/bin/python
import os
import sys 
import time
import spidev as SPI
from lib import RoundLCD
import touch_driver_1inch28 as Touch
from PIL import Image,ImageDraw,ImageFont


Font1 = ImageFont.truetype("Font/Font02.ttf",45)
Font2 = ImageFont.truetype("Font/Font02.ttf",20)


try:
    disp = RoundLCD.RoundLCD_HAT()
    
    Touch.touch_init() # initlize touch 
    
    disp.Init() # Initialize library.
    
    disp.clear() # Clear display.
    image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")
    draw = ImageDraw.Draw(image1)
    im_r=image1.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(1)
    image = Image.open('pic/lcd_logo.jpg')	
    im_r=image.rotate(0)
    disp.ShowImage(im_r)
    time.sleep(2)

    image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
    draw2 = ImageDraw.Draw(image2)
    while True:
                cd  = Touch.start_gesture()
                if cd == 'TAP' or cd == 'DOUBLE_TAP':
                        print("TAP")

                        
                if cd == 'FLICK UP':
                            print("UP")
                            image = Image.open('images/img1.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)

                elif cd == 'FLICK DOWN':
                            print("DOWN")
                            image = Image.open('images/img6.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                                    
                                    
                elif cd == 'FLICK LEFT':
                            print("LEFT")
                            image = Image.open('images/img7.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)
                      
                                    
                elif cd == 'FLICK RIGHT':
                            print("RIGHT")
                            image = Image.open('images/img2.jpg')	
                            im_r2=image.rotate(0)
                            disp.ShowImage(im_r2)

                     

                                    
except KeyboardInterrupt:
    disp.module_exit()
    exit()

