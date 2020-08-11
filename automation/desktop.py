import pyautogui as auto
import pandas as pd
import time

auto.FAILSAFE = False
screenWidth ,screenHeight  = auto.size()
auto.doubleClick(36,67)
time.sleep(4)
auto.press("ctrl"+"t")
# auto.press('t')