import requests

geoserver_url = "http://localhost:8080/geoserver/pedro/wms"

params = {
    "SERVICE": "WMS",
    "VERSION": "1.1.1",
    "REQUEST": "GetMap",
    "FORMAT": "image/png",
    "TRANSPARENT": "true",
    "STYLES": "",
    "LAYERS": "pedro:PB_Municipios_2023",
    "EXCEPTIONS": "application/vnd.ogc.se_inimage",
    "SRS": "EPSG:4674",
    "WIDTH": "768",
    "HEIGHT": "440",
    "BBOX": "-36.021766662597656,-7.0827484130859375,-35.758094787597656,-6.9316864013671875"
}

response = requests.get(geoserver_url, params=params)

if response.status_code == 200:
    # Se deu certo ele salva a imagem
    with open("esperanca_mapa.png", "wb") as file:
        file.write(response.content)
    print("Imagem salva como 'esperanca_mapa.png'.")
else:
    print(f"Erro ao obter imagem: {response.status_code}")
