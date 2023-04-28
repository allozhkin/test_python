from .command_abstract import Command


class CommandOpen(Command):
    # Данный класс реализует команду заполнение записной книжки из файла

    def description(self):
        return "Открыть записную книжку"

    def execute(self):
        self.console.open_notebook()