
from selenium import webdriver
# from selenium.webdriver.chrome import service
import pyautogui as auto
import pandas as pd
import time
# from browserautomation import OpenBrowser
from selenium import webdriver

auto.FAILSAFE = False
screenWidth ,screenHeight  = auto.size()
class OpenBrowser():
    def start(self):
        webdriver_service = service.Service('/home/kunal/Downloads/operadriver_linux64/operadriver')
        webdriver_service.start()
        driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
        driver.get('http://localhost:3000/signin')

    def startChrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("--start-maximized")
        # height = 0
        
        driver = webdriver.Chrome(executable_path='/home/kunal/Downloads/chromedriver_linux64/chromedriver', chrome_options=options)
        driver.get('http://localhost:3000/signin')
        curWindowHndl = driver.current_window_handle
        auto.size()
        auto.position()
        auto.click(600,180)
        auto.press('tab')
        auto.press('tab')
        auto.press('tab')
        auto.press('tab')
        auto.press('tab')
        auto.typewrite('ashutosh932@gmail.com',0.25)
        auto.press('tab')
        auto.typewrite('Abc@123',0.25)
        auto.press('tab')
        auto.press('enter')
        auto.PAUSE= 2.0
        
        # driver.close()
        # driver.close()
        driver.switch_to.window(curWindowHndl)
        # time.sleep(3)

OpenBrowser().startChrome()
time.sleep(3)
