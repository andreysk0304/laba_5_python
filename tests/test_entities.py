import pytest

from src.entities.player import Player
from src.entities.goose import Goose, WarGoose, HonkGoose
from src.entities.chip import Chip
from src.exceptions import ChipTypeError


class TestPlayer:
    def test_init(self):
        player = Player("Alice")
        assert player.name == "Alice"
        assert player.balance == 100

    def test_init_custom_balance(self):
        player = Player("Bob", 200)
        assert player.balance == 200

    def test_change_balance(self):
        player = Player("Alice")
        player.change_balance(50)
        assert player.balance == 150
        player.change_balance(-30)
        assert player.balance == 120

    def test_repr(self):
        player = Player("Alice", 150)
        repr_str = repr(player)
        assert "Alice" in repr_str
        assert "150" in repr_str


class TestGoose:
    def test_init(self):
        goose = Goose("Гусь1")
        assert goose.name == "Гусь1"
        assert goose.honk_volume == 1

    def test_init_custom_volume(self):
        goose = Goose("Гусь1", 5)
        assert goose.honk_volume == 5

    def test_honk(self):
        goose = Goose("Гусь1", 3)
        honk = goose.honk()
        assert "Гусь1" in honk
        assert "3" in honk

    def test_repr(self):
        goose = Goose("Гусь1")
        repr_str = repr(goose)
        assert "Goose" in repr_str
        assert "Гусь1" in repr_str


class TestWarGoose:
    def test_attack(self):
        goose = WarGoose("Боевой", 2)
        player = Player("Alice", 100)
        goose.attack(player)
        assert player.balance == 90  # 100 - (5 * 2)

    def test_attack_damage(self):
        goose = WarGoose("Боевой", 3)
        player = Player("Alice", 100)
        goose.attack(player)
        assert player.balance == 85  # 100 - (5 * 3)


class TestHonkGoose:
    def test_special_honk(self):
        goose = HonkGoose("Кричащий", 2)
        players = [Player("Alice", 100), Player("Bob", 100)]
        goose.special_honk(players)
        assert players[0].balance == 98  # 100 - 2
        assert players[1].balance == 98


class TestChip:
    def test_init(self):
        chip = Chip(10)
        assert chip.amount == 10

    def test_add(self):
        chip1 = Chip(10)
        chip2 = Chip(20)
        result = chip1 + chip2
        assert result.amount == 30
        assert isinstance(result, Chip)

    def test_add_type_error(self):
        chip = Chip(10)
        with pytest.raises(ChipTypeError):
            _ = chip + "не фишка"

    def test_add_type_error_int(self):
        chip = Chip(10)
        with pytest.raises(ChipTypeError):
            _ = chip + 5

    def test_repr(self):
        chip = Chip(50)
        repr_str = repr(chip)
        assert "50" in repr_str

