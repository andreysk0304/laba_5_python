import pytest

from src.casino import Casino
from src.entities.goose import Goose, WarGoose, HonkGoose
from src.exceptions import PlayerAlreadyExistsError, InsufficientPlayersError, InsufficientGeeseError, InsufficientWarGeeseError, InsufficientHonkGeeseError


class TestCasino:
    def test_register_player(self):
        casino = Casino()
        player = casino.register_player("Alice")
        assert player.name == "Alice"
        assert len(casino.players) == 1
        assert casino.balance["Alice"] == 100


    def test_register_player_duplicate(self):
        casino = Casino()
        casino.register_player("Alice")
        with pytest.raises(PlayerAlreadyExistsError):
            casino.register_player("Alice")


    def test_register_goose(self):
        casino = Casino()
        goose = Goose("Гусь1")
        casino.register_goose(goose)
        assert len(casino.geese) == 1
        assert goose in casino.geese


    def test_event_player_bet(self):
        casino = Casino()
        casino.register_player("Alice")
        initial_balance = casino.balance["Alice"]
        casino.event_player_bet()
        assert casino.balance["Alice"] < initial_balance


    def test_event_player_bet_no_players(self):
        casino = Casino()
        with pytest.raises(InsufficientPlayersError):
            casino.event_player_bet()


    def test_event_player_win(self):
        casino = Casino()
        casino.register_player("Alice")
        initial_balance = casino.balance["Alice"]
        casino.event_player_win()
        assert casino.balance["Alice"] > initial_balance


    def test_event_player_win_no_players(self):
        casino = Casino()
        with pytest.raises(InsufficientPlayersError):
            casino.event_player_win()


    def test_event_goose_attack(self):
        casino = Casino()
        casino.register_player("Alice")
        casino.register_goose(WarGoose("Боевой", 2))
        initial_balance = casino.balance["Alice"]
        casino.event_goose_attack()
        assert casino.balance["Alice"] < initial_balance


    def test_event_goose_attack_no_war_geese(self):
        casino = Casino()
        casino.register_player("Alice")
        casino.register_goose(HonkGoose("Кричащий", 1))
        with pytest.raises(InsufficientWarGeeseError):
            casino.event_goose_attack()


    def test_event_goose_attack_no_players(self):
        casino = Casino()
        casino.register_goose(WarGoose("Боевой", 2))
        with pytest.raises(InsufficientPlayersError):
            casino.event_goose_attack()


    def test_event_goose_honk(self):
        casino = Casino()
        casino.register_player("Alice")
        casino.register_goose(HonkGoose("Кричащий", 3))
        initial_balance = casino.balance["Alice"]
        casino.event_goose_honk()
        assert casino.balance["Alice"] < initial_balance


    def test_event_goose_honk_no_honk_geese(self):
        casino = Casino()
        casino.register_player("Alice")
        casino.register_goose(WarGoose("Боевой", 2))
        with pytest.raises(InsufficientHonkGeeseError):
            casino.event_goose_honk()


    def test_event_goose_honk_no_players(self):
        casino = Casino()
        casino.register_goose(HonkGoose("Кричащий", 1))
        with pytest.raises(InsufficientPlayersError):
            casino.event_goose_honk()


    def test_event_steal(self):
        casino = Casino()
        casino.register_player("Alice")
        casino.register_goose(Goose("Вор", 1))
        initial_balance = casino.balance["Alice"]
        casino.event_steal()
        assert casino.balance["Alice"] < initial_balance


    def test_event_steal_no_geese(self):
        casino = Casino()
        casino.register_player("Alice")
        with pytest.raises(InsufficientGeeseError):
            casino.event_steal()


    def test_event_steal_no_players(self):
        casino = Casino()
        casino.register_goose(Goose("Вор", 1))
        with pytest.raises(InsufficientPlayersError):
            casino.event_steal()


    def test_simulate_step(self):
        casino = Casino()
        casino.register_player("Alice")
        casino.register_goose(WarGoose("Боевой", 2))
        casino.register_goose(HonkGoose("Кричащий", 3))
        casino.register_goose(Goose("Обычный", 1))

        # Должно выполниться без ошибок
        casino.simulate_step()