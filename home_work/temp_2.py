from diplom_funcs import *
from diplom_class import Users
def found(filename, data):
    with open(filename, 'r', encoding='utf-8') as f:
        for el in f:
            if data in el:
                print(el, end='')





