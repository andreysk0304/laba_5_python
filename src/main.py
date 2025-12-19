import sys

from src.simulation import run_simulation
from src.command import Command
from src.exceptions import CommandNotFound


def run_loop() -> None:
    print('Добро пожаловать в cli "Андрюшка", команды можно посмотреть командой help, приятного использования')
    print('>', end='')

    for command_line_text in sys.stdin:
        try:
            if command_line_text.strip().lower() in ('break', 'quit', 'exit', 'stop'):
                break

            if command_line_text.strip().lower() == 'help':
                print('help - список команд\nrun 18 23 - запускается симуляция steps = 18, seed = 23, seed - не обязателен\n\nquit, exit, stop, break - отключить cli')
                continue

            cmd: Command = Command(command_line_text)

            if cmd.command in ('run_sim', 'run', 'sim', 'run_simulation'):
                run_simulation(steps=cmd.steps, seed=cmd.seed)
                continue

            raise CommandNotFound(cmd.command)
        except Exception as error:
            print(error)
        finally:
            print('>', end='')

    print('cli "Андрюшка" прекратил свою работу')

if __name__ == '__main__':
    run_loop()