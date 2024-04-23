import random
import time
import requests
import datetime

url = 'http://localhost/ti-project/api/api.php'
# Dicionário, onde as keys são os sensores e as values a range dos valores que serão gerados
sensors = {
    "temperatura": [0, 50],
    "humidade": [0, 100],
    "pressao": [500, 2000]
}

while True:
    # Tempo atual do PC para gerar a hora
    date = datetime.datetime.now().isoformat()

    # Para cada sensor
    for (sensor, value_range) in sensors.items():
        # Geramos um valor entre a range definida no dicionário
        # Por exemplo a temperatura irá gerar um valor aleatório entre [0, 50]
        value = random.randint(value_range[0], value_range[1])
        # Fazemos o request para a API para atualizarmos o valor
        request = requests.post(url, data={"nome": "{}".format(sensor), "valor": "{}".format(value), "hora": date})

        print("{}: {} @ {} ({})".format(sensor, value, date, request.status_code))

    print()

    # Esperamos um segundo e como estamos dentro do while loop, o código irá correr
    # infinitamente até o programa ser terminado
    time.sleep(1)
