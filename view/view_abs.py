# Модуль, реализующий абстрактный класс View
from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def set_presenter(self, presenter):
        """
        Aбстрактный метод, который должен принимать экземпляр класса-презентера
        (Presenter) в качестве аргумента.
        """

    @abstractmethod
    def start(self):
        """
        Aбстрактный метод, который должен выполнять начальную настройку консольного приложения и
        запускать его отображение.
        """