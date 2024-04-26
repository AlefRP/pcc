# from car import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2019)
# print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2019)
# print(my_leaf.get_descriptive_name())

# from car import * # Not recomended, to avoid name conflict
# import car

# my_mustang = car.Car('ford', 'mustang', 2019)
# print(my_mustang.get_descriptive_name())

# my_leaf = car.ElectricCar('nissan', 'leaf', 2019)
# print(my_leaf.get_descriptive_name())

# import eletric_car as ec
from car_new import Car
from eletric_car_v2 import ElectricCar as EC

my_mustang = Car('ford', 'mustang', 2019)
print(my_mustang.get_descriptive_name())

my_leaf = EC('nissan', 'leaf', 2019)
print(my_leaf.get_descriptive_name())