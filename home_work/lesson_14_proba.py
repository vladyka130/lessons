class F():

     def met_1(self, a, b):
         return  a + b

     @staticmethod
     def met_2(a, b):
         return a + b

a_1 = F()
print(a_1.met_1(1, 2))
print(F.met_2(1, 2))