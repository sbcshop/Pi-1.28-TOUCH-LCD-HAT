#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys 
import smbus
import time

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

# touch reset
GPIO.setup(23,GPIO.OUT) 
GPIO.output(23,GPIO.HIGH)

# touch intrrupt
#GPIO.setup(4, GPIO.IN)
Touch_int = 4 
GPIO.setup(Touch_int, GPIO.IN, pull_up_down=GPIO.PUD_UP)


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


PONT        = 0x08
GESTURES    = 0x80
TAP         = 0x20
FLICK       = 0x22
DOUBLE_TAP  = 0x23


UP          = 0x08
DOWN        = 0x0C
LEFT        = 0x0E
RIGHT       = 0x0A


UPPER_LEFT  = 0x0F
UPPER_RIGHT = 0x09
LOWER_LEFT  = 0x0D
LOWER_RIGHT = 0x0B
DOWN_LEFT   = 0xEC

COMMAND_BUFFER_INDEX   		= 0x20 
QUERY_BUFFER_INDEX		= 0x80
COMMAND_RESPONSE_BUFFER_INDEX   = 0xA0 
POINT_BUFFER_INDEX    		= 0xE0 
QUERY_SUCCESS     		= 0x00 
QUERY_BUSY     			= 0x01 
QUERY_ERROR     		= 0x02 
QUERY_POINT     		= 0x80



bus = smbus.SMBus(1) # i2c address of round touch
time.sleep(2) #wait here to avoid 121 IO Error
address = 0x46 # addrerss of round touch screen
DEVICE_ADDRESS = 0x46  

def Checktouch():
            for device in range(128):
               try:
                     bus.read_byte(0X46)
                     bus.read_byte(device)
                     #print(hex(device))
                     if device == address :
                         #open(bus)
                         print("touch device found")
                     else :
                         print("touch device not found")
                                     
               except: #exception if read_byte fails
                        #print("No device not found")
                        pass
                        



def CTP_CheckBusy():
        val = bus.read_byte_data(DEVICE_ADDRESS,QUERY_BUFFER_INDEX)
        return val

def CTP_IdentifyCapSen():
    ctpCheck = CTP_CheckBusy()
    if ctpCheck == 192 :
        print("touch busy")
    ret = bus.write_byte_data(DEVICE_ADDRESS,COMMAND_BUFFER_INDEX,1)
    if ret == 0:
        print("cmd_bufferindex falied")
    ctpCheck = CTP_CheckBusy()
    if ctpCheck == 192 :
        print("touch busy")
    '''
    data = bus.read_i2c_block_data(DEVICE_ADDRESS,COMMAND_RESPONSE_BUFFER_INDEX,10)
    print("data = ",data)
    lst = [10,73,84,69,55,50,53,57,50,48]
    
    for i in range(10):
        if (data[i]) == lst[i] :
            print("match data")
            return 1
        else :
            print("data not matched")
            return 0
    '''
    
    

def check_touch():
    ret = CTP_IdentifyCapSen()
    Checktouch()
    if ret == 1 :
        print("touch driver working fine")
    else :
        print("touch driver not working ")
    

def touch_init():
    ret = CTP_IdentifyCapSen()
    Checktouch()


def start_point():
        GPIO.wait_for_edge(Touch_int, GPIO.FALLING)
        
        bear = bus.read_i2c_block_data(address,128,1)
        bus.read_byte(0X46)
        #print(bus.read_byte_data(DEVICE_ADDRESS,0x80))
        #Stat = bus.read_i2c_block_data(DEVICE_ADDRESS,0x05,10)
        

        stat = bus.read_i2c_block_data(DEVICE_ADDRESS,POINT_BUFFER_INDEX,11)
        #print("status = ",stat)
        

        
        #def read_point_data():
        #def point():
        if stat[0] and PONT:
                    X = ((stat[3] and 0x0F) << 8) + stat[2]
                    Y = ((stat[3] and 0xF0) << 4) + stat[4]
                    return X,Y

                        


            

def start_gesture():
        GPIO.wait_for_edge(Touch_int, GPIO.FALLING)
        
        bear = bus.read_i2c_block_data(address,128,1)
        bus.read_byte(0X46)
        #print(bus.read_byte_data(DEVICE_ADDRESS,0x80))
        #Stat = bus.read_i2c_block_data(DEVICE_ADDRESS,0x05,10)
        

        stat = bus.read_i2c_block_data(DEVICE_ADDRESS,POINT_BUFFER_INDEX,11)
        #print("status = ",stat)
        

        
        #def read_point_data():
        #def point():
        '''
        if stat[0] and PONT:
                    X = ((stat[3] and 0x0F) << 8) + stat[2]
                    Y = ((stat[3] and 0xF0) << 4) + stat[4]
                    return X,Y
        '''
                        

        if stat[0] and GESTURES:
                if stat[1] == TAP or stat[1] == DOUBLE_TAP:
                            return "TAP"
                  
                if stat[1] == FLICK :
                    #return "FLICK"
                    if stat[10] == UP:
                            return "FLICK UP"

                    elif stat[10] == DOWN:
                            return "FLICK DOWN"
                                
                    elif stat[10] == RIGHT:
                            return "FLICK RIGHT"
                        
                    elif stat[10] == LEFT:
                            return "FLICK LEFT"
                 
                    elif stat[10] == LOWER_RIGHT:
                            return "FLICK LOWER RIGHT"

                    elif stat[10] == DOWN_LEFT:
                            return "FLICK DOWN LEFT"

                    elif stat[10] == UPPER_RIGHT:
                            return "FLICK UPPER_RIGHT"

                    elif stat[10] == UPPER_LEFT:
                            return "FLICK UPPER LEFT"

                                

                                



            

