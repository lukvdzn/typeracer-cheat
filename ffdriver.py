import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException

class FfDriverSession:
    __executable_path = "webdriver/geckodriver.exe"
    __driver = None

    def __init__(self):
        self.__driver = webdriver.Firefox(executable_path = self.__executable_path)

    def destroy_session(self):
        self.__driver.close()

    def get_url(self, url):
        self.__driver.get(url)

    def locate_elem_by_css(self, css):
        return self.__driver.find_element_by_css_selector(css)
    
    def locate_elems_by_css(self, css):
        return self.__driver.find_elements_by_css_selector(css)
    
    def wait_until_elem_by_css(self, css, max_delay = 5):
        try:
            return WebDriverWait(self.__driver, max_delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
        except TimeoutException:
            print("Exceeded maximum Waiting Time!")
            return None

    def exec_js(self, js):
        self.__driver.execute_script(js)

    def sim_key_in_session(self, *keys):
        # first find the main body container
        elem_body = self.__driver.find_element_by_xpath("//body")
        elem_body.send_keys(keys)

    def sleep_until_elem_located(self, time_dur):
        self.__driver.implicitly_wait(time_dur)
    
    def suspend_session_until(self, time_dur):
        time.sleep(time_dur)

    def sim_typing(self, word, interval):
        pyautogui.write(word, interval)