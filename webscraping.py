from selenium.common.exceptions import ElementNotInteractableException # Importei para compreender e tratar alguns erros durante o desenvolvimento
from selenium import webdriver # Importar Selenium para realizar ações que requerem interação com o site em questão

from time import sleep # Importar para inserir pausas durante a execução do programa, a fim de esperar que elementos da página sejam carregados
from selenium.webdriver.common.by import By # Importar esse mecanismo para utilizar o seletor e conseguir acessar os elementos HTML da página

#start = time.time()
url = 'https://veiculos.fipe.org.br/'

browser = webdriver.Chrome() # Inicializar o Chrome com webdriver
#browser.set_window_size(480, 720)
browser.get(url) # Acessar o site com a URL fornecida

query = browser.find_element(by=By.CLASS_NAME, value='ilustra') # Clicar na aba "Consulta de carros e utilitários pequenos"
query.click()

# Find all elements with class 'step-1'

brands = browser.find_elements(By.CSS_SELECTOR, '.step-1 option') # Acessar a div que define o primeiro input (Marca)
step2 = browser.find_element(By.CSS_SELECTOR, '.step-2') # Acessar a div que contém os outros inputs: Modelos dos veículos e Modelo por ano de cada veículo

# Loop through each <option> tag
for brand in brands: # Percorrer as marcas possíveis
    if brand.text != '':
        sleep(2)
        brand.click()
        print(brand.text)
        models = step2.find_elements(By.CSS_SELECTOR, '[urlconsulta="ConsultarAnoModelo"] option')

        for model in models: # Percorrer os modelos de veículos de cada marca
            if model.text != '':
                model.click()
                print(model.text)
                years = step2.find_elements(By.CSS_SELECTOR, '[urlconsulta="ConsultarModelosAtravesDoAno"] option')

                for year in years: # Percorrer os diversos modelos de diferentes anos de cada modelo de veículo
                    if year.text != '':
                        year.click()
                        print(year.text)

#--------------------------------------------------------------------------------------------------------------------------#

# Eu havia feito mais coisas no código, porém notei que a estrutura do site mudava de modo inesperado e acabei não dando continuidade por falta de tempo.
# Após coletar os dados ao acessar a Table renderizada após realizar a pesquisa, eu iria salvar os dados e utilizar a biblioteca Pandas para tratá-los, transformá-los
# em um Dataframe e assim salvá-los no formato JSON ou CSV.