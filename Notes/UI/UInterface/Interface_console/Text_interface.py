# Класс статичных констант, предусмотрен для локального изменения
# текстровых сообщений пользователю.


class TxtInterface:
    greeting = "Добро пожаловать не в Notepad--\nДля работы со мной выберите опцию ниже :\n"
    enter_title = "Enter title: "
    enter_note = "Enter your note: "
    is_empty = "Empty"
    first_menu = "\n\
            1 - Import Notes from file.csv;\n\
            2 - Export Notes to file.csv;\n\
            3 - Create a new Note;\n\
            4 - View all notes;\n\
            5 - View last note;\n\
            6 - Edit a Note;\n\
            7 - Delete a Note;\n\
            8 - Export Notes to file.json;\n\
            9 - Import Notes from file.json;\n\
            0 - Exit."
    enter_command = "Enter command: "
    not_save = "Not saved note!"
    goodbye = "Goodbye!"
    incorrect_input = "Incorrect unput"
    notes_imported = "Notes imported!"
    notes_empty = "Notes are empty!"
    notes_saved = "Notes saved!"
    show_notes = "All notes : "
    show_last = "Last note: "
    edit_note = "Enter Title note for edit: "
    current_title = "текущий заголоdок: "
    current_note = "текущяя заметка: "
    enter_ID = "Enter ID note for delete: "
    note_deleted = "Note deleted"
    not_file = "Not found file!"