import string, datetime

now = datetime.datetime.now()

def get_pib():
    pib = input("Введiть призвiще, iм'я та по-батьковi (не обов'язково) через пробiл: ")
    for i in pib:
        if i in string.digits:
            pib = pib.replace(i, '')
    pib = pib.title()
    print(pib)
    return pib

def get_gender():
    while True:
        gender = input("Введiть стать (Ч\Ж): >>> ").upper()
        if gender in 'ЧЖ':
            return gender


def get_birth():
    while True:
        birth = input('Введыть дату народження: рiк, мiсяць, день (через пробiл): >>> ').split()
        if ("".join(birth).isdigit() and 1900 <= int(birth[0]) <= now.year and 1 <= int(birth[1]) <= 12 and 1 <= int(birth[2]) <= 31):
            try:
                date = datetime.datetime(int(birth[0]), int(birth[1]), int(birth[2]))
                if now > date:
                    break
            except ValueError:
                print("Ввведіть коректно: ")
        else:
            print("Ввведіть коректно: ")
    return date

def get_death():
    while True:
        death = input('''Введiть дату смерті (якщо така існує): рiк, мiсяць, день (через пробiл) 
        якщо ще рано, то натисніть "Q" : >>> ''').upper().split()
        try:
            if death == ['Q']:
                return "---"
            death_date = datetime.datetime(int(death[0]), int(death[1]), int(death[2]))
            death_date_2 = now - death_date
            if death_date_2.days < 0:
                print(f'Death ERROR! дата смертi через {abs(death_date_2.days)} днiв? Звiдки знаете ? ')
                continue
            return death_date
        except Exception:
            print('ERROR! Введiть коректно: >>>')


def get_dth():
    try:
        dth_str = get_death().strftime("%Y-%m-%d")
    except AttributeError:
        dth_str = "----"
    return dth_str

#birth = get_birth().strftime("%Y-%m-%d")
def age():
    pass

def save_to_file(file_name, data):
    write_or_add = input("Хочете створити новий файл  - вкажiть 1\n якщо редагувати iснуючий - вкажiть 2\n >>>  ")
    # with open(file_name, 'w', encoding='utf-8') as f:
    #     f.write(data)
    #     f.close()

