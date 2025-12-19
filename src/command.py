from src.exceptions import ParseCommandError, ToManyParamsError, NotEnoughParametersError


class Command:

    def __init__(self, command_line_text) -> None:
        self.command_line_text = command_line_text

        self.command: str = ''
        self.seed: int | None = None
        self.steps: int = 5

        self._tokens = []

        self._parse_command()


    def _normalize_command_line_text(self) -> None:
        """
        Функиця нормализует входную строку (приводит все символы к строчному виду и убирает лишние символы )
        :return: Нормализованная строка
        """
        self.command_line_text = self.command_line_text.lower().strip()


    def _parse_command(self) -> None:
        """
        Функция распаршивает входную строку в команду и параметры, записывает результаты в переменную класса
        :return: Ничего
        """
        self._get_tokens()

        self._get_command()
        self._get_steps()

        self._get_seed()


    def _get_tokens(self) -> None:
        """
        Функция разбивает входную строку на токены и записывает в переменную класса для дальнейшего использования
        :return: Ничего
        """
        self._tokens += self.command_line_text.split()

        size = len(self._tokens)

        if size == 0:
            raise ParseCommandError()

        if size == 1:
            raise NotEnoughParametersError()

        if size > 3:
            raise ToManyParamsError()




    def _get_command(self) -> None:
        """
        Функция получает команду из токенов и записывает в переменную класса
        :return: Ничего
        """
        self.command = self._tokens[0]


    def _get_steps(self) -> None:
        """
        Функция получает кол-во шагов заданных пользователем из команды
        :return: Ничего
        """
        steps = self._tokens[1]

        try:
            self.steps = int(steps)
        except (TypeError, ValueError):
            raise TypeError('Введённое вами кол-во шагов должно быть целым числом!')

        return


    def _get_seed(self) -> None:
        """
        Функция получает seed, заданный пользователем в команде ( если задан ) и записывает в переменную класса
        :return: Ничего
        """

        if len(self._tokens) < 3:
            return

        seed = self._tokens[2]

        try:
            self.seed = int(seed)
        except (ValueError, TypeError):
            raise TypeError('Введённый вами seed должен быть целым числом!')

        return