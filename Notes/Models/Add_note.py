# Класс компоненты, которая принимает ввод пользователя
# из консоли и формирует экземпляр типа Note (заметка)


from Models.Note import Note
from UI.UInput.input_console.Input_note import Input_console_note


class Add_new_note:
    def __init__(self):
        self.note = Note()

    def add_note(self):
        note_input = Input_console_note()
        note_input.input_note()
        self.note.title = note_input.title
        self.note.body = note_input.body