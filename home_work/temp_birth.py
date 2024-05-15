import datetime

now = datetime.datetime.now()

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

birth_str = get_birth().strftime("%Y-%m-%d")