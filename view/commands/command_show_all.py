from .command_abstract import Command


class CommandShowAll(Command):
    # Данный класс реализует команду вывода всех заметок в консоль

    def description(self):
        return "Показать все заметки"

    def execute(self):
        self.console.show_all()