import datetime

now = datetime.datetime.now()
def get_birth():
    visokosniy = [2024, 2020, 2016, 2012, 2008, 2004, 2000, 1996, 1992, 1988, 1984, 1981, 1980, 1908, 1912, 1916,
                  1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976]
    while True:
        birth = input('Введыть дату народження: рiк, мiсяць, день (через пробiл): >>> ').split()
        if ("".join(birth).isdigit() and 1900 <= int(birth[0]) <= now.year and 1 <= int(birth[1]) <= 12 and 1 <= int(birth[2]) <= 31
                 and (int(birth[0]) in visokosniy and 1 <= int(birth[2]) < 30)):
            date = datetime.datetime(int(birth[0]), int(birth[1]), int(birth[2]))
            if now > date:
                break
        else:
            print("Ввведіть коректно: ")
    return date

birth_str = get_birth().strftime("%Y-%m-%d")

# age = now - birth
