Para utilizar esta ferramenta, é necessário instalar o selenium e suas dependências (como por exemplo, o WebDriver, para ser possível manusear de forma automatizada seu browser).
O intuito desse programa é, de forma automatizada, coletar as informações referentes a cada veículo de diferentes marcas, com diferentes modelos de diferentes anos. As informações coletadas são:
 - Marca
- Modelo
- Ano Modelo
- Combustível
- Código Fipe
- Preço Médio

As informações de todos veículos devem ser armazenadas em um arquivo único de formato JSON ou CSV, para que os dados sejam coletados e mais facilmente manipulados através de ferramentas de análise.
O arquivo gerado através das informações obtidas pelo webscraping será salvo com o nome de "dados_fipe", com a terminação dependente do formato escolhido.

As informações serão coletadas através da ação automatizada do Selenium, junto à capacidade de manusear dados, do Pandas. Com essas duas bibliotecas e com o intermédio da linguagem de programação
Python, é possível coletar os dados, tratar os mesmos e armazená-los num arquivo, tudo isso de forma estruturada.
