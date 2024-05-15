import datetime

now = datetime.datetime.now()

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

def get_dth(st):
    try:
        dth_str = get_death().strftime("%Y-%m-%d")
    except AttributeError:
        dth_str = "----"
    st = int(birth[:3])
    if dth_str != "----" and st < int(dth_str[0:3]):
        return dth_str
    else:
        print("Дата смертi ранiше народження ?")
        return "-----"

