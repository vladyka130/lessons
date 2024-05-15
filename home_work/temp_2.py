import datetime
now = datetime.datetime.now()
def get_death():
    while True:
        death = input('''Введiть дату смерті (якщо така існує): рiк, мiсяць, день (через пробiл)
        якщо не усніє натисніть "Q" : >>> ''').split()
        if death == 'Q':
            return ''


print(get_death())