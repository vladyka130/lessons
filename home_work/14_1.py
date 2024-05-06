class My_class():

    @staticmethod
    def first(a, b):
        return a + b

print(My_class.first(4,5))

# 45:30     @classmethod

class Avto():
    Total_object = 0

    def __init__(self, mark):
        self.mark = mark
        self.calc_object()
    @classmethod
    def calc_object(cls):
        cls.Total_object +=1            # СТУКАЕМОСЬ ДО АТРИБУТУ КЛАСУ

a_1 = Avto('BMW-3')
a_2 = Avto('lada')
a_3 = Avto('ural')
print(Avto.Total_object) # сккыльки створено обектыв
print(a_2.Total_object)