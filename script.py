import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException


with webdriver.Firefox(executable_path='webdriver/geckodriver.exe') as driver:
    driver.get("https://play.typeracer.com/")
    delay = 5
    try:
        # first locate enter race "button"
        elem_enter_race = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.gwt-Anchor')))
        # remove unwanted cookies acceptance dialogs, which cover most of the screen
        js = """var cookieaccept = document.querySelector('.qc-cmp-ui-container');
                if(cookieaccept) cookieaccept.parentNode.removeChild(cookieaccept)"""
        driver.execute_script(js)
        # send enter race key shortcut to browser
        elem_body = driver.find_element_by_xpath("//body")
        elem_body.send_keys(Keys.CONTROL, Keys.ALT, 'i')
        # fetch given text to write
        # wait until given text appears
        time.sleep(15)
        #input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.txtInput[maxlength='11']")))
        elem_text_parts = driver.find_elements_by_css_selector("span[unselectable='on']")
        # there may be sentences starting with 'I', so a space has to be added
        text = None
        if len(elem_text_parts) == 2:
            text = elem_text_parts[0].text + " " + "".join([elem.text for elem in elem_text_parts[1:]])
        else:
            text = elem_text_parts[0].text + " " + elem_text_parts[1].text + " " + "".join([elem.text for elem in elem_text_parts[2:]])
        print(text)
        pyautogui.write(text, interval=0.1)
    except TimeoutException:
        print("Loading took too much time!")
    