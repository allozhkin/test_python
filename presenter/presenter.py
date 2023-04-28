# Модуль, реализующий класс Presenter

from model.file_manager import FileManager


class Presenter:
    def __init__(self, view, notebook, path: str):
        self.__view = view
        self.__notebook = notebook
        self.__view.set_presenter(self)
        self.file = FileManager(path)

    def open_file(self):
        # Чтение файла и заполнение записной книжки
        self.__notebook = self.file.file_read(self.__notebook)

    def save(self):
        # Запись изменений в файл
        self.file.file_write(self.__notebook)

    def is_full(self):
            # Проверяет, заполнена ли записная книжка.

        return self.__notebook.is_full()

    def add_note(self, title_text: str, text_note: str):
        # Добавление новой заметки в записную книжку.
        self.__notebook.add_note(title_text, text_note)

    def remove_note(self, index: int):
        # Удаление заметки из записной книжки по указанному индексу.
        self.__notebook.remove_note(index)

    def change_note(self, index: int, update_title: str, update_text: str):
        # Редактирование заметки по указанному индексу
        self.__notebook.change_note(index, update_title, update_text)

    def get_size_notebook(self):
        # Возвращает размер записной книжки (длину списка)
        return self.__notebook.size()

    def get_tabl_notebook(self):
        # Возвращает строковое представление записной книжки в виде таблицы
        return self.__notebook.tabl

    def get_filtered_tabl(self, date: str):
        # Возвращает строковое представление записной книжки в виде таблицы,
        # отфильтрованной по дате
        return self.__notebook.filter_by_date(date)
