class Player:
    def __init__(self, name: str, balance: int = 100):
        self.name = name
        self.balance = balance

    def change_balance(self, amount: int):
        """
        Изменяет баланс игрока
        :param amount: Сумма на которую изменяется баланс
        :return: Ничего
        """
        if not isinstance(amount, int):
            raise TypeError('Сумма должна быть целым числом.')
        self.balance += amount

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, balance={self.balance})"