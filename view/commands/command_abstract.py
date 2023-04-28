from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, console):
        self.console = console

    @abstractmethod
    def description(self):
        """Aбстрактный метод, который должен возвращать описание команды."""

    @abstractmethod
    def execute(self):
        """Aбстрактный метод, который должен выполнять действия, связанные с выполнением команды."""
