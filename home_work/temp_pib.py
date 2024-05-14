def get_pib():
    pib = input("Введiть призвiще, iм'я та по-батьковi (не обов'язково) через пробiл: ")
    for i in pib:
        if i in string.digits:
            pib = pib.replace(i, '')
    pib = pib.title()
    print(pib)
    return pib

pibs= get_pib()