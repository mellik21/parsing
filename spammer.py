import time
import pyautogui
from random import randint
import secret

while True:
    time.sleep(5)

    pyautogui.typewrite(secret.words[randint(0, 6)])
    pyautogui.press("enter")
