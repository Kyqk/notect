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