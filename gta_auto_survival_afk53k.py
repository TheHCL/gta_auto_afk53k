import pydirectinput as p
import keyboard as k
import time
import os
import pyautogui as py 
import ctypes as c

def d_click():                  #direct input for mouse
    c.windll.user32.mouse_event(2, 0,0,0,0)
    time.sleep(0.01)
    c.windll.user32.mouse_event(4, 0,0,0,0)


def job():  # idle auto with direct input
    p.keyDown('w')
    time.sleep(1)
    p.keyUp('w')
    p.keyDown('s')
    time.sleep(1)
    p.keyUp('s')
    p.keyDown('a')
    time.sleep(1)
    p.keyUp('a')
    p.keyDown('d')
    time.sleep(1)
    p.keyUp('d')

def test():   # where i use to test my left click
    d_click()
    time.sleep(1)
    d_click()
    time.sleep(1)
    d_click()

def check():  # to check if the mission is complete and replay after complete
    play = py.locateCenterOnScreen("gta_pic/play.PNG",confidence = 0.9)
    time.sleep(1)
    replay = py.locateCenterOnScreen("gta_pic/replay.PNG",confidence = 0.9)
    time.sleep(1)
    if play is not None:
        py.moveTo(play)
        time.sleep(1)
        d_click()
    
        
    
    if replay is not None:
        py.moveTo(replay)
        time.sleep(1)
        d_click()


# i am the main function===============================
time.sleep(10)
while 1:
    check()
    job()
    if k.is_pressed('2'):
        break

