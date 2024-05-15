from diplom_funcs import *
from diplom_class import Users
def save_to_file(data):
    while True:
        write_or_add = input(" Хочете створити новий файл  - натиснiть 1\n якщо редагувати iснуючий    - натиснiть 2\n >>>  ")
        if write_or_add == "1":
            mode = 'w'
            file = input("Вкажiть назву файлу? >>> ")
            if file[-4:] != '.txt':
                file = file + '.txt'
            break
        elif write_or_add == "2":
            mode = 'a'
            file = input("Вкажiть файл? >>> ")
            if file[-4:] != '.txt':
                file = file + '.txt'
            break
        else:
            print("То який обираэте режим? >>>")
    print(file)
    with open(file=file, mode=mode, encoding='utf-8') as f:
        f.write(data)
        f.close()
