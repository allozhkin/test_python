from .command_abstract import Command


class CommandExit(Command):

    def description(self):
        return "Завершить работу"

    def execute(self):
        self.console.finish()
