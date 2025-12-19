from src.exceptions import PlayerNotFoundError


class CasinoBalance:
    def __init__(self, balances = None):
        self._balances = dict(balances) if balances else {}

    def __getitem__(self, key):
        if key not in self._balances:
            raise PlayerNotFoundError(key)
        return self._balances[key]

    def __setitem__(self, key, value):
        print(f"[LOG] Баланс {key} изменён → {value}")
        self._balances[key] = value

    def __delitem__(self, key):
        if key not in self._balances:
            raise PlayerNotFoundError(key)
        print(f"[LOG] Баланс {key} удалён")
        del self._balances[key]

    def __iter__(self):
        return iter(self._balances.items())

    def __len__(self):
        return len(self._balances)

    def __repr__(self):
        return f"{self.__class__.__name__}(balances={self._balances})"