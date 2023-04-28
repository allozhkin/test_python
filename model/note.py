# Модуль, реализующий класс создания заметки и работы с ней.
from datetime import datetime


class Note:
    # Класс для создания заметки.
    # Атрибуты:
    # __title (str): текст заголовка заметки.
    # __text_note (str): текст заметки.
    # __creation_data (str): дата/время создания заметки.
    # __changes_data (str): дата/время последнего изменения заметки
    # Методы:
    # 1. __init__: конструктор класса для создания заметки.
    # 1. get_title: возвращает заголовок заметки.
    # 2. get_creation_data: возвращает дату и время создания заметки.
    # 3. get_changes_data: возвращает дату и время последнего изменения заметки.
    # 4. get_text_note: возвращает текст-содержание заметки.
    # 5. change: изменение заметки.

    def __init__(self, title: str, creation_data: str, text_note: str, changes_data: str = ''):
        self.__title = title
        self.__text_note = text_note
        self.__creation_data = creation_data
        self.__changes_data = changes_data

    def get_title(self):
        return self.__title

    def get_creation_data(self):
        return self.__creation_data

    def get_changes_data(self):
        return self.__changes_data

    def get_text_note(self):
        return self.__text_note

    def change(self, title: str, new_text: str):
        if title:
            self.__title = title
        if new_text:
            self.__text_note = new_text
        self.__changes_data = datetime.today().strftime('%d.%m.%Y %H:%M')
