from .command_abstract import Command


class CommandChange(Command):
    def description(self):
        return "Изменить заметку"

    def execute(self):
        self.console.change_note()