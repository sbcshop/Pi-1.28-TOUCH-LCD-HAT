#!/usr/bin/python
import os
import sys 
import time
import spidev as SPI
from lib import RoundLCD
from lib import touch_driver_1inch28 as Touch
from PIL import Image,ImageDraw,ImageFont

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay1 = 21
relay2 = 26
relay3 = 19
relay4 = 13
relay5 = 6
relay6 = 5

GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)
GPIO.setup(relay4,GPIO.OUT)
GPIO.setup(relay5,GPIO.OUT)
GPIO.setup(relay6,GPIO.OUT)

GPIO.output(relay1,GPIO.LOW)
GPIO.output(relay2,GPIO.LOW)
GPIO.output(relay3,GPIO.LOW)
GPIO.output(relay4,GPIO.LOW)
GPIO.output(relay5,GPIO.LOW)
GPIO.output(relay6,GPIO.LOW)


Font1 = ImageFont.truetype("Font/Font00.ttf",25)
Font2 = ImageFont.truetype("Font/Font02.ttf",20)


request1 = 0;
flag_1=0;

request2 = 0;
flag_2=0;

request3 = 0;
flag_3=0;

request4 = 0;
flag_4=0;


request5 = 0;
flag_5=0;

request6 = 0;
flag_6=0;

request7 = 0;
flag_7=0;

try:
    #Warning!!!Don't  creation of multiple displayer objects!!! '''
    disp = RoundLCD.RoundLCD_HAT()
    
    Touch.touch_init() # initlize touch 
    
    disp.Init() # Initialize library.
    
    disp.clear() # Clear display.

    r = 24
    r1 = 25
    x, y = 30, 110
    x1, y1 = 90, 110
    x2, y2 = 150, 110
    x3, y3 = 210, 110
    x4, y4 = 60, 170

    r2 = 12
    x5, y5 = 120, 170
    x6, y6 = 180, 170

                    
    image2=Image.new("RGB", (disp.width, disp.height), (0,132,203))
    draw2 = ImageDraw.Draw(image2)
    draw3 = ImageDraw.Draw(image2)

    draw2.ellipse([(x-r, y-r), (x+r, y+r)], fill = 'orange', outline ='black')
            
    draw2.ellipse([(x1-r, y1-r), (x1+r, y1+r)], fill = 'orange', outline ='black')
                    
    draw2.ellipse([(x2-r, y2-r), (x2+r, y2+r)], fill = 'orange', outline ='black')
                    
    draw2.ellipse([(x3-r, y3-r), (x3+r, y3+r)], fill = 'orange', outline ='black')
            
    draw2.ellipse([(x4-r, y4-r), (x4+r, y4+r)], fill = 'orange', outline ='black')

    draw2.ellipse([(x5-r, y5-r), (x5+r, y5+r)], fill = 'orange', outline ='black')

    draw2.ellipse([(x6-r, y6-r), (x6+r, y6+r)], fill = 'orange', outline ='black')
 
    draw2.arc((1,1,240,240),0, 360, fill =(255,51,153), width=2)

    #draw2.text((X,Y), "*", font=Font2, fill = (255,255,255))
    
    draw2.text((38,30), "PRESS BUTTON", font=Font1, fill = (255,255,0))
    
    disp.ShowImage(image2)

    while True:
            cd = Touch.start_point() # start touch
            #print(cd)
            if cd == None:
                continue
            X,Y = cd
            #print("x = " + str(X),"y = "+str(Y))
                    

            
           ##############################################

           #############################################
        
            if X >= 1 and X <= 44 and Y >= 78 and Y <= 122:
                       request1 = "button1"
                       if request1 == "button1":
                          if flag_1 == 0:                     
                            flag_1=1
                            print("BUTTON 1 ON")
                            GPIO.output(relay1,GPIO.HIGH)
                            draw3.ellipse([(x-r, y-r), (x+r, y+r)], fill = 'green', outline ='black')
                            disp.ShowImage(image2)
                          
                          elif flag_1 == 1:
                            flag_1=0
                            print("BUTTON 1 OFF")
                            GPIO.output(relay1,GPIO.LOW)
                            draw3.ellipse([(x-r, y-r), (x+r, y+r)], fill = 'red', outline ='black')
                            
                            disp.ShowImage(image2)
                            
                    

                         
            
            elif X >= 63 and X <= 108 and Y >= 78 and Y <= 122:
                       request2 = "button2"
                       if request2 == "button2":
                          if flag_2 == 0:                     
                             flag_2=1
                             print("BUTTON 2 ON")
                             GPIO.output(relay2,GPIO.HIGH)
                             draw2.ellipse([(x1-r, y1-r), (x1+r, y1+r)], fill = 'green', outline ='black')
                             disp.ShowImage(image2)
                          
                          elif flag_2 == 1:                   
                            flag_2=0
                            print("BUTTON 2 OFF")
                            GPIO.output(relay2,GPIO.LOW)
                            draw2.ellipse([(x1-r, y1-r), (x1+r, y1+r)], fill = 'red', outline ='black')
                            disp.ShowImage(image2)
                            

            
            elif X >= 125 and X <= 168 and Y >= 78 and Y <= 122:
                       request3 = "button3"
                       if request3 == "button3":
                          if flag_3 == 0:                     
                             flag_3=1
                             print("BUTTON 3 ON")
                             GPIO.output(relay3,GPIO.HIGH)
                             draw2.ellipse([(x2-r, y2-r), (x2+r, y2+r)], fill = 'green', outline ='black')
                             disp.ShowImage(image2)
                          
                          elif flag_3 == 1:                   
                             flag_3=0
                             print("BUTTON 3 OFF")
                             GPIO.output(relay3,GPIO.LOW) 
                             draw2.ellipse([(x2-r, y2-r), (x2+r, y2+r)], fill = 'red', outline ='black')
                             disp.ShowImage(image2)

                        

            elif X >= 183 and X <= 225 and Y >= 78 and Y <= 122:
                       request4 = "button4"
                       if request4 == "button4":
                          if flag_4 == 0:                     
                             flag_4=1
                             print("BUTTON 4 ON")
                             GPIO.output(relay4,GPIO.HIGH)
                             draw2.ellipse([(x3-r, y3-r), (x3+r, y3+r)], fill = 'green', outline ='black')
                             disp.ShowImage(image2)
                          
                          elif flag_4 == 1:                   
                             flag_4=0
                             print("BUTTON 4 OFF")
                             GPIO.output(relay4,GPIO.LOW)
                             draw2.ellipse([(x3-r, y3-r), (x3+r, y3+r)], fill = 'red', outline ='black')
                             disp.ShowImage(image2)

                        
            
            elif X >= 36 and X <= 74 and Y >= 137 and Y <= 180:
                       request5 = "button5"
                       if request5 == "button5":
                          if flag_5 == 0:                     
                             flag_5=1
                             print("BUTTON 5 ON")
                             GPIO.output(relay5,GPIO.HIGH) 
                             draw2.ellipse([(x4-r, y4-r), (x4+r, y4+r)], fill = 'green', outline ='black')
                             disp.ShowImage(image2)
                          
                          elif flag_5 == 1:                   
                             flag_5=0
                             print("BUTTON 5 OFF")
                             GPIO.output(relay5,GPIO.LOW)
                             draw2.ellipse([(x4-r, y4-r), (x4+r, y4+r)], fill = 'red', outline ='black')
                             disp.ShowImage(image2)


            elif X >= 94 and X <= 135 and Y >= 137 and Y <= 180:
                       request6 = "button6"
                       if request6 == "button6":
                          if flag_6 == 0:                     
                             flag_6=1
                             print("BUTTON 6 ON")
                             GPIO.output(relay6,GPIO.HIGH)
                             draw2.ellipse([(x5-r, y5-r), (x5+r, y5+r)], fill = 'green', outline ='black')
                             disp.ShowImage(image2)
                          
                          elif flag_6 == 1:                   
                             flag_6=0
                             print("BUTTON 6 OFF")
                             GPIO.output(relay6,GPIO.LOW)
                             draw2.ellipse([(x5-r, y5-r), (x5+r, y5+r)], fill = 'red', outline ='black')
                             disp.ShowImage(image2)


            elif X >= 153 and X <= 197 and Y >= 137 and Y <= 180:
                       request7 = "button7"
                       if request7 == "button7":
                          if flag_7 == 0:                     
                             flag_7=1
                             print("BUTTON 7 ON")
                             draw2.ellipse([(x6-r, y6-r), (x6+r, y6+r)], fill = 'green', outline ='black')
                             disp.ShowImage(image2)
                              
                          elif flag_7 == 1:                   
                             flag_7=0
                             print("BUTTON 7 OFF")
                             draw2.ellipse([(x6-r, y6-r), (x6+r, y6+r)], fill = 'red', outline ='black')
                             disp.ShowImage(image2)

                
       
except KeyboardInterrupt:
    disp.module_exit()
    exit()

