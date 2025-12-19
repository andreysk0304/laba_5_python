from src.entities.goose import Goose
from src.exceptions import GooseNotFoundError, IndexOutOfRangeError


class GooseCollection:
    def __init__(self, geese=None):
        self._geese = list(geese) if geese else []

    def add(self, goose):
        """
        Добавляет нового гуся в коллекцию
        :param goose: Гусь (экземпляр класса гуся)
        :return: Ничего
        """
        print(goose)
        if not isinstance(goose, Goose):
            raise TypeError(f'Вы пытаетесь добавить не гуся в коллецию гусей! Тип: {type(goose)}')
        self._geese.append(goose)

    def remove(self, goose):
        """
        Удаляет гуся из коллекции если он есть
        :param goose: Гусь (экземпляр класса гуся)
        :return: Ничего
        """
        if goose not in self._geese:
            raise GooseNotFoundError(goose.name if hasattr(goose, 'name') else None)
        self._geese.remove(goose)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._geese[index]
        if index < 0 or index >= len(self._geese):
            raise IndexOutOfRangeError(index, len(self._geese))
        return self._geese[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= len(self._geese):
            raise IndexOutOfRangeError(index, len(self._geese))
        self._geese[index] = value

    def __delitem__(self, index):
        if index < 0 or index >= len(self._geese):
            raise IndexOutOfRangeError(index, len(self._geese))
        del self._geese[index]

    def __iter__(self):
        return iter(self._geese)

    def __len__(self):
        return len(self._geese)

    def __contains__(self, goose):
        return goose in self._geese

    def __repr__(self):
        return f"{self.__class__.__name__}(geese={self._geese})"

    def __add__(self, other):
        return GooseCollection(self._geese + list(other))