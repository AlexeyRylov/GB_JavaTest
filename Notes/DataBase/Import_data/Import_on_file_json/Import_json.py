
import json
from Models.Note import Note
from Presenter.P_console.P_user_data.Printer import Printer
from UI.UInterface.Interface_console.Path import Path
from UI.UInterface.Interface_console.Text_interface import TxtInterface

class Import_json:
    def __init__(self):
        self.input_data = []


    def read_file(self):
        with open(Path.PATH_JSON) as json_file:
            self.input_data = json.load(json_file)
            Printer(TxtInterface().notes_imported).prints()


    def parse_input(self):
        self.parse_data = []
        for item in self.input_data['Note']:# type: ignore
            note = Note()
            note.set(item['ID'], item['Title'], item['Note'], item['Date'])
            self.parse_data.append(note)