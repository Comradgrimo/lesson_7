# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Dress(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def get_square(self):
        pass

    @property
    def get_square_full(self):
        return str(f'Площадь общая ткани {(2 * self.height + 0.3) + (self.width / 6.5 + 0.5)}')


class Coat(Dress):
    def get_square(self):
        return self.width / 6.5 + 0.5

    def __str__(self):
        return f'Площадь на пальто {self.get_square()}'


class Jacket(Dress):
    def get_square(self):
        return self.height * 2 + 0.3

    def __str__(self):
        return f'Площадь на костюм {self.get_square()}'
    pass


class FullCost(Dress):
    def get_square(self):
        return (2 * self.height + 0.3) + (self.width / 6.5 + 0.5)

    @property
    def get_square_full(self):
        return str(f'Площадь общая ткани {self.get_square()}')


jacket = Jacket(70, 10)
coat = Coat(70, 10)
cost = FullCost(70, 10)

print(cost.get_square_full)
print(jacket)
print(coat)