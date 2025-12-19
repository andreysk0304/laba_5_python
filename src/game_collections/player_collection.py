from src.entities.player import Player
from src.exceptions import PlayerNotFoundError, IndexOutOfRangeError


class PlayerCollection:
    def __init__(self, players = None):
        self._players = list(players) if players else []

    def add(self, player):
        """
        Добавляет нового игрока в коллекцию
        :param player: Экземпляр класса игрока
        :return: Ничего
        """
        if not isinstance(player, Player):
            raise TypeError('Вы пытаетесь положить не пользователя в коллекцию пользователей.')
        self._players.append(player)

    def remove(self, player):
        """
        Удаляет игрока из коллекции
        :param player: Экземпляр класса игрока
        :return: Ничего
        """
        if player not in self._players:
            raise PlayerNotFoundError(player.name if hasattr(player, 'name') else None)
        self._players.remove(player)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._players[index]
        if index < 0 or index >= len(self._players):
            raise IndexOutOfRangeError(index, len(self._players))
        return self._players[index]

    def __delitem__(self, index):
        if index < 0 or index >= len(self._players):
            raise IndexOutOfRangeError(index, len(self._players))
        del self._players[index]

    def __iter__(self):
        return iter(self._players)

    def __len__(self):
        return len(self._players)

    def __repr__(self):
        return f"{self.__class__.__name__}(players={self._players})"
