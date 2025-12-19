import pytest

from src.game_collections.player_collection import PlayerCollection
from src.game_collections.goose_collection import GooseCollection
from src.game_collections.balance_dict import CasinoBalance
from src.entities.player import Player
from src.entities.goose import Goose, WarGoose, HonkGoose
from src.exceptions import PlayerNotFoundError,GooseNotFoundError, IndexOutOfRangeError


class TestPlayerCollection:
    def test_add_and_len(self):
        pc = PlayerCollection()
        assert len(pc) == 0
        pc.add(Player("Alice"))
        assert len(pc) == 1
        pc.add(Player("Bob"))
        assert len(pc) == 2

    def test_getitem(self):
        pc = PlayerCollection([Player("Alice"), Player("Bob")])
        assert pc[0].name == "Alice"
        assert pc[1].name == "Bob"

    def test_getitem_slice(self):
        pc = PlayerCollection([Player("A"), Player("B"), Player("C")])
        result = pc[0:2]
        assert len(result) == 2
        assert result[0].name == "A"

    def test_getitem_out_of_range(self):
        pc = PlayerCollection([Player("Alice")])
        with pytest.raises(IndexOutOfRangeError):
            _ = pc[10]

    def test_iter(self):
        pc = PlayerCollection([Player("Alice"), Player("Bob")])
        names = [p.name for p in pc]
        assert names == ["Alice", "Bob"]

    def test_remove(self):
        pc = PlayerCollection([Player("Alice"), Player("Bob")])
        player = pc[0]
        pc.remove(player)
        assert len(pc) == 1

    def test_remove_not_found(self):
        pc = PlayerCollection([Player("Alice")])
        with pytest.raises(PlayerNotFoundError):
            pc.remove(Player("Bob"))

    def test_delitem(self):
        pc = PlayerCollection([Player("Alice"), Player("Bob")])
        del pc[0]
        assert len(pc) == 1
        assert pc[0].name == "Bob"

    def test_delitem_out_of_range(self):
        pc = PlayerCollection([Player("Alice")])
        with pytest.raises(IndexOutOfRangeError):
            del pc[10]


class TestGooseCollection:
    def test_add_and_len(self):
        gc = GooseCollection()
        assert len(gc) == 0
        gc.add(Goose("Гусь1"))
        assert len(gc) == 1

    def test_getitem(self):
        gc = GooseCollection([Goose("Гусь1"), Goose("Гусь2")])
        assert gc[0].name == "Гусь1"
        assert gc[1].name == "Гусь2"

    def test_getitem_out_of_range(self):
        gc = GooseCollection([Goose("Гусь1")])
        with pytest.raises(IndexOutOfRangeError):
            _ = gc[5]

    def test_remove_not_found(self):
        gc = GooseCollection([Goose("Гусь1")])
        with pytest.raises(GooseNotFoundError):
            gc.remove(Goose("Гусь2"))

    def test_contains(self):
        goose = Goose("Гусь1")
        gc = GooseCollection([goose])
        assert goose in gc
        assert Goose("Другой") not in gc

    def test_add_operation(self):
        gc1 = GooseCollection([Goose("Гусь1")])
        gc2 = GooseCollection([Goose("Гусь2")])
        result = gc1 + gc2
        assert len(result) == 2


class TestCasinoBalance:
    def test_setitem_and_getitem(self):
        cb = CasinoBalance()
        cb["Alice"] = 100
        assert cb["Alice"] == 100

    def test_getitem_not_found(self):
        cb = CasinoBalance()
        with pytest.raises(PlayerNotFoundError):
            _ = cb["Несуществующий"]

    def test_delitem(self):
        cb = CasinoBalance()
        cb["Alice"] = 100
        del cb["Alice"]
        assert len(cb) == 0

    def test_delitem_not_found(self):
        cb = CasinoBalance()
        with pytest.raises(PlayerNotFoundError):
            del cb["Несуществующий"]

    def test_len(self):
        cb = CasinoBalance()
        assert len(cb) == 0
        cb["Alice"] = 100
        assert len(cb) == 1
        cb["Bob"] = 200
        assert len(cb) == 2

    def test_iter(self):
        cb = CasinoBalance({"Alice": 100, "Bob": 200})
        items = dict(cb)
        assert items == {"Alice": 100, "Bob": 200}

