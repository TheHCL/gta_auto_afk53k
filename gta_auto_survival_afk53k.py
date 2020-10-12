import pydirectinput as p
import keyboard as k
import time
import os
import pyautogui as py 
import ctypes as c

flag =0

def d_click():                  #direct input for mouse
    c.windll.user32.mouse_event(2, 0,0,0,0)
    time.sleep(0.01)
    c.windll.user32.mouse_event(4, 0,0,0,0)


def job():  # no use
    p.keyDown('w')
    time.sleep(0.5)
    p.keyUp('w')
    p.keyDown('s')
    time.sleep(0.5)
    p.keyUp('s')
    time.sleep(5)

def playtab():   
    play2 = py.locateOnScreen("gta_pic/play2.PNG",confidence = 0.8,grayscale =True)
    global flag
    if play2 is None:
        p.press("s")
        time.sleep(0.1)

        
    else:  
        p.keyDown('enter')
        time.sleep(0.02)
        p.keyUp('enter')
        flag = 1
        time.sleep(5)
    
def replaytab():
    replay1 = py.locateCenterOnScreen("gta_pic/replay1.PNG",confidence = 0.7,grayscale=True)
    global flag

    if replay1 is None:
        p.press("s")
        time.sleep(0.1)
        
    else:  
        p.keyDown('enter')
        time.sleep(0.02)
        p.keyUp('enter')
        time.sleep(5)
        flag = 2
        
def play2tab():
    play3 = py.locateCenterOnScreen("gta_pic/play3.PNG",confidence = 0.9,grayscale=True)
    global flag

    if play3 is None:
        p.press("s")
        time.sleep(0.1)
        
    else:  
        p.keyDown('enter')
        time.sleep(0.02)
        p.keyUp('enter')
        time.sleep(5)
        flag = 0        


    
        
    

def check():  # add flag to determine which script to run
    global flag
    if flag == 0:
        playtab()
        print("Set up")
    if flag == 1:
        replaytab()
        print("In Game")
    
    if flag == 2:
        play2tab()
        print("set up 2")


# i am the main function===============================

time.sleep(10)
while 1:
    check()
    
    
    if k.is_pressed('*'):
        break

