import json
import datetime

filename = 'notes.json'

def load_notes():
    try:
        with open(filename, 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(filename, 'w') as f:
        json.dump(notes, f)

def get_notes(query=None):
    notes = load_notes()
    if query:
        notes = [note for note in notes if note['date'] == query]
    if not notes:
        print("Заметки отсутствуют!")
    return notes

def view_note(note_id):
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        return note
    else:
        return None    

def add_note():
    notes = load_notes()
    note_title = input("Введите заголовок заметки: ")
    note_text = input("Введите текст заметки: ")
    note_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    note_id = len(notes) + 1
    notes.append({'id': note_id, 'title': note_title, 'text': note_text, 'date': note_date})
    save_notes(notes)

def edit_note():
    notes = load_notes()
    note_id = int(input("Введите номер заметки для редактирования: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        note_title = input("Введите новый заголовок заметки: ")
        note_text = input("Введите новый текст заметки: ")
        note_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        note['title'] = note_title
        note['text'] = note_text
        note['date'] = note_date
        save_notes(notes)
    else:
        print("\nЗаметка не найдена!")    

def delete_note():
    notes = load_notes()
    note_id = int(input("Введите номер заметки для удаления: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        notes.remove(note)
        save_notes(notes)
        print("\nЗаметка удалена!")
    else:
        print("\nЗаметка не найдена!")        