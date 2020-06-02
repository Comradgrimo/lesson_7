#Тут посложнее, не совсем понял зандания
from abc import ABC, abstractmethod


class Dress(ABC):
    @property
    def value(self):
        return self._value

    def __init__(self, value):
        self._value = value

    def __new__(cls, *args, **kwargs):
        if cls is Dress:
            raise TypeError(
                "Can't instantiate abstract class {name} directly".format(name=cls.__name__)
            )
        return object.__new__(cls)

    @abstractmethod
    def get_square(self):
        pass


class Coat(Dress):
    def get_square(self):
        return self.value / 6.5 + 0.5

    def __str__(self):
        return 'Площадь на пальто %s' % self.get_square()


class Jacket(Dress):
    def get_square(self):
        return 2 * self.value + 0.3

    def __str__(self):
        return 'Площадь на костюм %s' % self.get_square()


class Foo(object):
    pass


jacket = Jacket(20)
coat = Coat(20)

real_value = jacket.get_square() + coat.get_square()
order = [jacket, coat, Foo(), 10]
test = 0
for item in order:
    if isinstance(item, Dress):
        test += item.get_square()
print(jacket)
print(coat)
print(test)

