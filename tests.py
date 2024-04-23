import random
import time
import requests
import datetime

url = 'http://localhost/ti-project/api/api.php'
# Dicion�rio, onde as keys s�o os sensores e as values a range dos valores que ser�o gerados
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
        # Geramos um valor entre a range definida no dicion�rio
        # Por exemplo a temperatura ir� gerar um valor aleat�rio entre [0, 50]
        value = random.randint(value_range[0], value_range[1])
        # Fazemos o request para a API para atualizarmos o valor
        request = requests.post(url, data={"nome": "{}", "valor": "{}".format(sensor, value), "hora": date})

        print("{}: {} @ {} ({})".format(sensor, value, date, request.status_code))

    print()

    # Esperamos um segundo e como estamos dentro do while loop, o c�digo ir� correr
    # infinitamente at� o programa ser terminado
    time.sleep(1)
