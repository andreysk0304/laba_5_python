from src.entities.player import Player


class Goose:
    def __init__(self, name: str, honk_volume: int = 1):
        self.name = name
        self.honk_volume = honk_volume

    def honk(self):
        """
        Воспроизводит крик гуся (образно)
        :return: Ничего
        """
        return f"{self.name} ОРЁТ с громкостью {self.honk_volume} дб"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"


class WarGoose(Goose):
    def attack(self, player):
        """
        Наносит урон определённому экземпляру игрока
        :param player: Экземпляр класса игрока
        :return: Строка лог действия
        """
        damage = 5 * self.honk_volume
        if not isinstance(player, Player):
            raise TypeError('Вы пытаетесь изменить баланс не игроку')
        player.change_balance(-damage)
        return f"{self.name} атакует {player.name} и отнимает {damage} монет!"


class HonkGoose(Goose):
    def special_honk(self, players):
        """
        Наносит урон своим криком сразу всем игрокам в коллекции игроко
        :param players: Коллекция всех игроков в игре
        :return: Строка лог действия
        """
        effect = -self.honk_volume

        for p in players:
            if isinstance(p, Player):
                p.change_balance(effect)
            else:
                raise TypeError('Вы пытаетесь изменить баланс не игроку.')

        return f"{self.name} устраивает крик! Все игроки теряют {abs(effect)} монет :D"