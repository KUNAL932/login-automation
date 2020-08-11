
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
        # driver.get('http://localhost:3000/signin')
        driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        curWindowHndl = driver.current_window_handle
        # auto.size()
        # auto.position()
        auto.click(600,332)
        # auto.press('tab')
        # auto.press('tab') 
        # auto.press('tab') 
        # auto.press('tab')
        # auto.press('tab') s
        time.sleep(3)
        auto.typewrite('kunalkashyap932@gmail.com',2)
        auto.press('tab')
        auto.press('enter')
        auto.PAUSE = 2.9
        auto.click(600,329)
        # auto.press('tab')
        auto.typewrite('**********',2)
        auto.press('tab')
        auto.press('enter')
        auto.PAUSE= 3.0
        # curWindowHndl = driver.current_window_handle
        driver.close()  
        # driver.close()
        # driver.switch_to.window(curWindowHndl)
        # time.sleep(3)

OpenBrowser().startChrome()


