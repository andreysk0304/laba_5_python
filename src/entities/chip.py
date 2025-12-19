from src.exceptions import ChipTypeError


class Chip:
    def __init__(self, amount: int):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Chip):
            raise ChipTypeError(type(other))

        return Chip(self.amount + other.amount)

    def __repr__(self):
        return f"{self.__class__.__name__}(amount={self.amount})"