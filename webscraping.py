from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup #Importar BeautifulSoup - Manusear o HTML obtido da página
from selenium import webdriver

from time import sleep
import time
from selenium.webdriver.common.by import By

#start = time.time()
url = 'https://veiculos.fipe.org.br/'

browser = webdriver.Chrome()
#browser.set_window_size(480, 720)
browser.get(url)

query = browser.find_element(by=By.CLASS_NAME, value='ilustra')
query.click()

# Find all elements with class 'step-1'

brands = browser.find_elements(By.CSS_SELECTOR, '.step-1 option')
step2 = browser.find_element(By.CSS_SELECTOR, '.step-2')

# Loop through each <option> tag
for brand in brands:
    if brand.text != '':
        sleep(2)
        brand.click()
        print(brand.text)
        models = step2.find_elements(By.CSS_SELECTOR, '[urlconsulta="ConsultarAnoModelo"] option')

        for model in models:
            if model.text != '':
                model.click()
                print(model.text)
                years = step2.find_elements(By.CSS_SELECTOR, '[urlconsulta="ConsultarModelosAtravesDoAno"] option')

                for year in years:
                    if year.text != '':
                        year.click()
                        print(year.text)

#end = time.time()
#execution_time = end - start
#print(f'Execution time: {execution_time} seconds.')