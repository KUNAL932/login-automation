import pyautogui as auto
import pandas as pd
import time
from browserautomation import OpenBrowser
from selenium import webdriver

auto.FAILSAFE = False
screenWidth ,screenHeight  = auto.size()

print(screenWidth,screenHeight)
OpenBrowser().startChrome()
# auto.move(876,424)
# auto.pause(2)
# auto.screenshot('/home/kunal/Downloads/screen.png')
# sc_chrome_x, sc_chrome_y =auto.locateCenterOnScreen(r'/home/kunal/Downloads/screen.png')
# time.sleep(2)
auto.size()
auto.position()
auto.click(600,180)
auto.press('tab')3
auto.typewrite('ashutosh932@gmail.com',2.0)
auto.press('tab')
auto.typewrite('Abc@123')
auto.press('tab')
auto.click(724,347)

# driver.quit()
# auto.click(732,359)

# auto.hotkey('tab')

# auto.typewrite('ashutosh932@gmail.com')