# Модуль, реализующий класс для создания записной книжки с заметками и работы с ней
from datetime import datetime

from tabulate import tabulate

from .note import Note


class Notebook:

    # Класс для создания записной книжки с заметками.
    #     Атрибуты:
    #     __notes (list): список заметок.
    #     Методы и свойства:
    #     1. __init__: конструктор класса для создания записной книжки.
    #     2. get_notes: возвращает список заметок.
    #     3. add_note: добавить новую заметку в записную книжку.
    #     4. size: получить длину списка заметок.
    #     5. remove_note: удалить заметку из списка.
    #     6. change_note: изменить заметку.
    #     7. is_full: проверить заполнена ли записная книжка.
    #     8. tabl: возвращает содержание записной книжки в виде таблицы.
    #     9. filter_by_date: возвращает содержание записной книжки в виде таблицы, отфильтрованной
    #     по дате.

    def __init__(self):
        self.__notes = []

    def size(self):
        return len(self.__notes)

    def add_note(self, title: str, text_note: str):
        note = Note(title, datetime.today().strftime(
            '%d.%m.%Y %H:%M'), text_note)
        self.__notes.append(note)

    def remove_note(self, index: int):
        del self.__notes[index]

    def change_note(self, index: int, title: str, update_text: str):
        self.__notes[index].change(title, update_text)

    def is_full(self):
        return bool(self.__notes)

    def get_notes(self):
        return self.__notes

    @property
    def tabl(self):
        headers = ['№', 'Заголовок', 'Заметка',
                   'Дата/время создания', 'Дата/время изменения']
        tabl = [[i, note.get_title(), note.get_text_note(),
                 note.get_creation_data(), note.get_changes_data()]
                for i, note in enumerate(self.__notes, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')

    def filter_by_date(self, date: str):
        headers = ['№', 'Заголовок', 'Заметка',
                   'Дата/время создания', 'Дата/время изменения']
        tabl = [[i, note.get_title(), note.get_text_note(), note.get_creation_data(),
                 note.get_changes_data()] for i, note in enumerate(self.__notes, start=1)
                if date in note.get_creation_data() or date in note.get_changes_data()]
        return tabulate(tabl, headers=headers, tablefmt="fancy_grid", stralign='center')
