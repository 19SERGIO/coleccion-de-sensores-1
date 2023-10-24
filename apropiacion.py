import pymongo
import colorama
import random
import time

conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["apropiacion-sensores"]
sensores = bd["sensores"]


lista_sensores = list(sensores.find())

med_fue_rango = 0  # mediciones fuera de rango

while med_fue_rango < 3:
    sensor = random.choice(lista_sensores)
    valor = random.uniform(sensor["minimo"], sensor["maximo"])
    
    if sensor["minimo"] <= valor <= sensor["maximo"]:
        print(colorama.Fore.GREEN + f"{sensor['nombre']}: {valor}" + colorama.Style.RESET_ALL)
    else:
        print(colorama.Fore.RED + f"{sensor['nombre']}: {valor}" + colorama.Style.RESET_ALL)
        med_fue_rango += 1
    time.sleep(1)