def get_gender():
    while True:
        gender = input("Введiть стать (Ч\Ж): >>> ").upper()
        if gender in 'ЧЖ':
            return gender

gnd = get_gender()
print(gnd)