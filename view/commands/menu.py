from .command_add import CommandAdd
from .command_change import CommandChange
from .command_exit import CommandExit
from .command_filter import CommandFilter
from .command_open import CommandOpen
from .command_remove import CommandRemove
from .command_save import CommandSave
from .command_show_all import CommandShowAll


class Menu:
    # Данный класс создает основное меню и реализует запуск методов

    def __init__(self, console):
        self.commands = []
        self.commands.append(CommandOpen(console))
        self.commands.append(CommandShowAll(console))
        self.commands.append(CommandFilter(console))
        self.commands.append(CommandAdd(console))
        self.commands.append(CommandChange(console))
        self.commands.append(CommandRemove(console))
        self.commands.append(CommandSave(console))
        self.commands.append(CommandExit(console))

    def __str__(self):
        menu_string = "\n======== Главное меню ========\n"
        for i, cmd in enumerate(self.commands, start=1):
            menu_string += f"\t{i}. {cmd.description()}\n"
        return menu_string

    def get_size_menu(self):
        return len(self.commands)

    def execute(self, index: int):
        option = self.commands[index]
        option.execute()
