# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class My(ABC):
    @abstractmethod                 #Реализуем абстрактрый метод
    def get_square(self):
        pass

class Dress(My):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def get_square(self):
        return str(f'Площадь общая ткани {self.width + self.width}')


class Coat(Dress):                  # Класс обязательно должен иметь иплекацию? метода get_squary класса My
    def get_square(self):
        return self.width / 6.5 + 0.5
    def __str__(self):
        return f'Площадь на пальто {self.get_square()}'


class Jacket(Dress):                # Класс обязательно должен иметь иплекацию? метода get_squary класса My
    def get_square(self):
        return 2 * self.height + 0.3
    def __str__(self):
        return f'Площадь на костюм {self.get_square()}'

d = Dress(10,20)
print(d.get_square)

jacket = Jacket(10, 20)
coat = Coat(10, 20)
print(jacket)
print(coat)