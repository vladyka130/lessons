def func(x):
    x = x.replace(",", ".")

    if x.isdigit():
        print("ціле додатнє")
    elif x[0] == "-" and x[1:].isdigit():
        print("ціле від'ємне")
    elif x[0] == "-" and "." in x and x.count(".") < 2:
        print("від'ємне дробове")
    elif "." in x and x.count(".") < 2:
        print("додатнє дробове")
    else:
        print("error")


while True:
    my_enter = input("Введіть число  або  'e/q' для виходу з програми:  ").lower()
    if my_enter in ['q', 'e', 'й', 'у']:
        print("Buy")
        break
    func(my_enter)