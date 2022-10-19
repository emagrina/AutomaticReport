# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from report_auth import *
from report_settings import *

# Opciones
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('---disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')



driver_path = _driver_path

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Start
driver.get('https://outlook.live.com/owa/')

WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'nav.auxiliary-actions > ul > li > a.internal.sign-in-link'))) \
    .click()

# Register email
WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input#i0116'))) \
    .send_keys(_email)

WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input#idSIButton9'))) \
    .click()

WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input#i0118'))) \
    .send_keys(_passw)

WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input#idSIButton9'))) \
    .click()

WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input#idBtn_Back'))) \
    .click()

# New message
WebDriverWait(driver, 30) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       "//span[contains(text(), 'Correo nuevo')]"))) \
    .click()

WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'div.YyuKd.pNWpr >div.G4a5Z > div.AALfT> div.QdX2d.VOlRn'))) \
    .send_keys(_addressee['email'])

WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input.ms-TextField-field'))) \
    .send_keys(_preference['title'])

WebDriverWait(driver, 10) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'div#editorParent_1 > div > div'))) \
    .send_keys(_preference['header'],
               _preference['content'],
               _preference['footer'],
               Keys.UP,
               Keys.UP)


