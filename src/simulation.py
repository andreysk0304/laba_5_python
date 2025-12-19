import random

from src.casino import Casino
from src.entities.goose import WarGoose, HonkGoose


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    """
    Функция запускает симуляцию игры
    :param steps: Кол-во шагов в симуляции
    :param seed: Сид симуляции ( при вводе одного и того же сида исход игры всегда будет одним)
    :return: Ничего
    """
    if seed is not None:
        random.seed(seed)

    casino = Casino()

    casino.register_player("Alice")
    casino.register_player("Bob")
    casino.register_player("Charlie")

    casino.register_goose(WarGoose("Гусяра намба ван", 2))
    casino.register_goose(HonkGoose("ГУСЫНЯ ( жена Гусяры )", 3))
    casino.register_goose(HonkGoose("просто гусь ю-ю", 1))

    print(f"Симуляция запущена! (seed = {seed if seed is not None else 'не задан'}, steps = {steps})")
    # ОШИБКА 1: Ошибка границы цикл, а должно быть range(steps), а не range(1, steps)
    for step in range(1, steps):
        print(f"\nШаг {step + 1}")
        casino.simulate_step()
    print("\nСИМУЛЯЦИЯ ОКОНЧЕНА")
