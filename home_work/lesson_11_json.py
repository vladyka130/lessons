# Створити словник як ключ якого буде 6-ти значне число,
# а в якості значень кортеж що складається з 2-х елементів - ім'я (str), вік (int).
# Зробити близько 5-6 елементів словника.
# Записати цей словник на диск у json-файл.

import json

my_dict = {'111111': ('Bob', 11),
           '222222': ('Jimm', 22),
           '333333': ('Hans', 33),
           '444444': ('Billy', 44),
           '555555': ('Jack', 55),
           '666666': ('John', 66)
           }

with open('my_first.json', 'w') as file:
    json.dump(my_dict, file)
