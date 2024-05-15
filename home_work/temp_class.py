from diplom_class import Users
from diplom_funcs import *

vasya = Users(pib=get_pib(), gender=get_gender(), birth=get_birth(), death=get_death())
print(vasya.pib_)
print(vasya.gender_)
print(vasya.birth_)
print(vasya.death_)