import random

from src.game_collections.player_collection import PlayerCollection
from src.game_collections.goose_collection import GooseCollection
from src.game_collections.balance_dict import CasinoBalance
from src.entities.player import Player
from src.entities.goose import WarGoose, HonkGoose
from src.exceptions import InsufficientPlayersError, InsufficientGeeseError, InsufficientWarGeeseError, InsufficientHonkGeeseError, PlayerAlreadyExistsError


class Casino:
    def __init__(self):
        self.players = PlayerCollection()
        self.geese = GooseCollection()
        self.balance = CasinoBalance()


    def register_player(self, name: str):
        """
        Функция которая регистрирует нового игрока в игру
        :param name: Имя игрока
        :return: Экземпляр класса игрока
        """
        # ОШИБКА 4: Сравнение через is вместо ==
        # if name is "Alice" or name is "Bob" or name is "Charlie":
        #     raise PlayerAlreadyExistsError(name)
        if name in [p.name for p in self.players]:
            raise PlayerAlreadyExistsError(name)
        p = Player(name)
        self.players.add(p)
        self.balance[p.name] = p.balance
        return p


    def register_goose(self, goose):
        """
        Функция регистрирует гуся в коллекцию гусей
        :param goose: Экземпляр класса гуся
        :return: Ничего
        """
        self.geese.add(goose)


    def event_player_bet(self):
        """
        Функция имитирует случайную проигранную ставку случайного игрока из коллекции
        :return: Ничего
        """
        if not self.players:
            raise InsufficientPlayersError("ставка")
        player = random.choice(self.players)
        bet = random.randint(5, 20)
        # ОШИБКА 5: Перепутанные аргументы, должно быть -bet, а не bet
        # player.change_balance(bet)
        player.change_balance(-bet)
        self.balance[player.name] = player.balance
        print(f"{player.name} делает ставку {bet}")


    def event_player_win(self):
        """
        Функция имитирует случайную выигранную ставку случайного игрока из коллекции
        :return: Ничего
        """
        if not self.players:
            raise InsufficientPlayersError("выигрыш")
        player = random.choice(self.players)
        win = random.randint(10, 40)
        player.change_balance(win)
        self.balance[player.name] = player.balance
        print(f"{player.name} выигрывает {win}")


    def event_goose_attack(self):
        """
        Функция имитирует атаку гуся на случайного игрока и снимает у него баланс (здоровье)
        :return: Ничего
        """
        war_geese = [g for g in self.geese if isinstance(g, WarGoose)]
        print(war_geese)
        print([x.name for x in war_geese])
        if not war_geese:
            raise InsufficientWarGeeseError()
        if not self.players:
            raise InsufficientPlayersError("атака гуся")
        goose = random.choice(war_geese)
        player = random.choice(self.players)
        print(goose.attack(player))
        self.balance[player.name] = player.balance


    def event_goose_honk(self):
        """
        Фкнция имитирует крик случайного гуся, из за чего балансы игроков уменьшаются
        :return: Ничего
        """
        honk_geese = [g for g in self.geese if isinstance(g, HonkGoose)]
        if not honk_geese:
            raise InsufficientHonkGeeseError()
        if not self.players:
            raise InsufficientPlayersError("крик гуся")
        goose = random.choice(honk_geese)
        msg = goose.special_honk(self.players)
        print(msg)
        # ОШИБКА 3: Изменение коллекции во время итерации
        # for p in self.players:
        #     if p.balance <= 0:
        #         self.players.remove(p)
        #     self.balance[p.name] = p.balance
        for p in self.players:
            self.balance[p.name] = p.balance


    def event_steal(self):
        """
        Функция имитирует кражу, случайный игрок крадёт у другого случайного игрока случайную сумму денег от 1 до 10 монет
        :return: Ничего
        """
        # ОШИБКА 2: Неверное логическое условие, перепутаны проверки и исключения
        # if not self.players:
        #      raise InsufficientGeeseError("кража")
        # if not self.geese:
        #     raise InsufficientPlayersError("кража")
        if not self.geese:
            raise InsufficientGeeseError("кража")
        if not self.players:
            raise InsufficientPlayersError("кража")
        goose = random.choice(self.geese)
        player = random.choice(self.players)
        stolen = random.randint(1, 10)
        player.change_balance(-stolen)
        print(f"{goose.name} крадёт {stolen} у {player.name}")
        self.balance[player.name] = player.balance


    def simulate_step(self):
        """
        Функция имитирует шаг симуляции, выбирает один из 5 ивентов в игре
        :return: Ничего
        """
        events = [
            self.event_player_bet,
            self.event_player_win,
            self.event_goose_attack,
            self.event_goose_honk,
            self.event_steal,
        ]

        random.choice(events)()
