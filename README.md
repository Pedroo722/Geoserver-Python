# Geoserver WMS - Shapefile dos Municípios da Paraíba

Como parte de uma atividade para a disciplina de Banco de Dados II, este repositório contém a configuração e código para execução local do GeoServer, publicação de uma camada a partir de um shapefile dos municípios da Paraíba e uma aplicação que consome o serviço WMS para requisitar uma imagem da cidade de Esperança em escala 1:136K.

## Tecnologias utilizadas


<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![GeoServer](https://img.shields.io/badge/GeoServer-0084C8?style=for-the-badge&logo=geoserver&logoColor=white)
![Shapefile](https://img.shields.io/badge/Shapefile-FFA500?style=for-the-badge&logo=geospatial&logoColor=white)
![WMS](https://img.shields.io/badge/WMS-009688?style=for-the-badge&logo=webgis&logoColor=white)

</div>

## Estrutura das páginas

A pasta ```codigo``` contém o script python para acessar o serviço WMS e requisitar a imagem da cidade de Esperança

A pasta ```geoserver-2.26.2-bin``` contém a aplicação do GeoServer extraída.

A pasta ```PB_Municipios_2023``` contém os arquivos referentes aos municípios da Paraíba.

## Depedências

1.

## Como Executar

1. Clone o repositório:
   ```fish
   git clone https://github.com/Pedroo722/Geoserver-Python.git
   cd Geoserver-Python/
   ```

2. Instale a depedência:
   ```fish
   python -m venv venv # Caso queira baixar a depedência em um ambiente venv
   source venv/bin/activate # Ativa o ambiente virtual

   python -m pip install requests
   ```


2. Execute o GeoServer localmente:
   ```fish
    cd geoserver-2.26.2-bin/
    java -jar start.jar
   ```

   Acesse a aplicação em: [http://localhost:8080/geoserver](http://localhost:8080/geoserver).

   E então faça login usando as credenciais padrão.
   
   **Username**: ```admin```
   
   **Password**: ```geoserver```


4. Crie um workspace (pedro). Adicione um store de um arquivo shapefile dos municípios da Paraíba (PB_Municipios_2023) e então publique uma camada a partir do shapefile cadastrado.


5. Execute a aplicação em Python:
   ```fish
   cd ../ # Caso ainda esteja no diretório do geoserver
   cd codigo/ # Para ir para o diretório do código.

   python App.py
   ```
