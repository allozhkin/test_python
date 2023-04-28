from .command_abstract import Command


class CommandFilter(Command):
    # Класс реализует команду фильтрации заметок по дате добавления или изменения

    def description(self):
        return "Сделать выборку заметок по дате"

    def execute(self):
        self.console.show_filtered_notebook()
