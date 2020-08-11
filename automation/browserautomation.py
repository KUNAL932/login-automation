
from selenium import webdriver
# from selenium.webdriver.chrome import service
import time
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
        driver.current_window_handle
        # driver.switch_to.window(curWindowHndl)
        # time.sleep(3)

        