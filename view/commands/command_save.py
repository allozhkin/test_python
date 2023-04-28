from .command_abstract import Command


class CommandSave(Command):
    # Данный класс реализует выполнения команды - сохранение изменений в записной книжке в файл

    def description(self):
        return "Сохранить изменения"

    def execute(self):
        self.console.save_changes()