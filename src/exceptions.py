class ParseCommandError(Exception):
    """Пустая строка в командной строке"""
    def __init__(self):
        super().__init__('Вы передали пустую строку')


class CommandNotFound(Exception):
    """Не известная команда"""
    def __init__(self, command: str):
        super().__init__(f'Команда "{command}" не существует')


class ToManyParamsError(Exception):
    """Слишком много параметров для команды"""
    def __init__(self):
        super().__init__('Вы ввели слишком большое кол-во параметров для команды')


class NotEnoughParametersError(Exception):
    """Не достаточное кол-во параметров"""
    def __init__(self):
        super().__init__('Вы ввели не достаточное кол-во параметров для команды')


class PlayerNotFoundError(Exception):
    """Игрок не найден в коллекции"""
    def __init__(self, player_name: str = None):
        if player_name:
            super().__init__(f'Игрок "{player_name}" не найден')
        else:
            super().__init__('Игрок не найден')


class GooseNotFoundError(Exception):
    """Гусь не найден в коллекции"""
    def __init__(self, goose_name: str = None):
        if goose_name:
            super().__init__(f'Гусь "{goose_name}" не найден')
        else:
            super().__init__('Гусь не найден')


class IndexOutOfRangeError(Exception):
    """Индекс вне допустимого диапазона"""
    def __init__(self, index: int, collection_size: int):
        super().__init__(
            f'Индекс {index} вне диапазона [0, {collection_size - 1}]\n(размер коллекции: {collection_size})'
        )


class InsufficientPlayersError(Exception):
    """Недостаточно игроков для выполнения операции"""
    def __init__(self, operation: str = None):
        if operation:
            super().__init__(f'Недостаточно игроков для операции: {operation}')
        else:
            super().__init__('Недостаточно игроков для выполнения операции')


class InsufficientGeeseError(Exception):
    """Недостаточно гусей для выполнения операции"""
    def __init__(self, operation: str = None):
        if operation:
            super().__init__(f'Недостаточно гусей для операции: {operation}')
        else:
            super().__init__('Недостаточно гусей для выполнения операции')


class InsufficientWarGeeseError(Exception):
    """Недостаточно боевых гусей (WarGoose) для выполнения операции"""
    def __init__(self):
        super().__init__('Недостаточно боевых гусей (WarGoose) для выполнения операции')


class InsufficientHonkGeeseError(Exception):
    """Недостаточно кричащих гусей (HonkGoose) для выполнения операции"""
    def __init__(self):
        super().__init__('Недостаточно кричащих гусей (HonkGoose) для выполнения операции')


class PlayerAlreadyExistsError(Exception):
    """Игрок с таким именем уже зарегистрирован"""
    def __init__(self, player_name: str):
        super().__init__(f'Игрок с именем "{player_name}" уже зарегистрирован в казино')


class ChipTypeError(Exception):
    """Ошибка типа при работе с фишками"""
    def __init__(self, other_type: type):
        super().__init__(f'Невозможно сложить фишку (Chip) с объектом типа {other_type.__name__}.\nОжидается объект типа Chip')