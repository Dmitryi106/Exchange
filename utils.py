# Открываем файл и загружаем его содержимое в переменную data
import json

with open('operations.json',encoding='utf8') as file:
    data = json.load(file)