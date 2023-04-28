from .command_abstract import Command


class CommandAdd(Command):
    # Класс реализует команду добавления заметки

    def description(self):
        return "Добавить заметку"

    def execute(self):
        self.console.add_note()