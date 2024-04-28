# class Dog:
#     color = 'Red'
#
#     def __init__(self, number_of_foot, tail, name):
#         self.tail = tail
#         self.name = name
#         self.number_of_foot = number_of_foot
#
#
#     def say(self):
#         print('woof')
#
#     def go(self):
#         for item in range(1, self.number_of_foot + 1):
#             print(f'step on {item} foot ', end='-')
#         print()
#
# #dog_1 = Dog()
# #dog_2 = Dog()
#
# #dog_2.tail = False
# #print(dog_1.tail)
# #print(dog_2.tail)
# #dog_3 = Dog()
# #dog_3.age = 3
# #print(dog_3.age)
# print('******************************************')
# dog_4 = Dog(4, False, 'Tuzik')
# print(dog_4.name)

class Cat(Dog):                                           #  успадкування класу Cat від  Dog
    def __init__(self, number_of_foot, tail, name ):      # додавання від батьківського ше свій шоб не писати всі свої такі самі
        super().__init__(number_of_foot, tail)
        super().say()                                     # визов метода батьківського класу
        self.name = name

    def say(self):
        print('miay')

class Woman(object):
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age                     # _ захищений атрибут
        self.__weight = weight              #   приватний атрибут. треба  стукатись w_1._Woman__weight

w_1 = Woman('Sussy', 26, 55)