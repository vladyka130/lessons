class F():

    def __init__(self):
        self.c = 0

    def met_1(self, a, b):
        return a + b + self.c

    @staticmethod                                # обризаэ обовязковий self
    def met_2(a, b):
        return a + b

a_1 = F()
print(a_1.met_1(1, 2))
print(F.met_2(1, 2))