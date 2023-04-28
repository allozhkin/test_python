from .command_abstract import Command


class CommandRemove(Command):
    # Класс реализует удаление заметки

    def description(self):
        return "Удалить заметку"

    def execute(self):
        self.console.remove_note()
