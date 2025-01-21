import serial
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time

while True:
    for i in range(20):
        num = random.randint(1,10)
        if num <= 5:
            keyboard.press('a')
            num = random.uniform(0.2, 0.4)
            time.sleep(num)
            keyboard.release('a')
            print('a')
        else:
            keyboard.press('d')
            num = random.uniform(0.2, 0.4)
            time.sleep(num)
            keyboard.release('d')
            print('d')