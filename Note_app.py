"""creating a base class"""
class Note:
"""Initialiing the class"""
    def __init__(self, note_id, content, created_at)
        self.note_id = note_id #Note ID
        self.content = content #Content of the note
        self.created_at = created_at #time created
        
"""creating the display() method"""
    def display(self) #defines display method
        print(self.note_id + "created at" + self.created_at ) #displays message
"""Extending base class"""
""" A textnote, a sub_class of Note"""
class TextNote(Note): #creates text note class
""" Initializing"""
    def __init__(self, text, time_created)
        self.text = text  #text in note
        self.time_created = time_created  #time note was created
""" Adding dispay method"""
    def display(self) #defines display for Textnote
        print("this is a text note") #displays message
""" A ReminderNote, a sub_class of Note"""
class ReminderNote(Note) #create reminder note class
"""Initializing"""
    def __init__(self, reminder_text, date, time) 
        self.message = reminder_text #title of reminder
        self.date = date  #date of reminder
        self.time = time #time of reminder
"""Adding display method"""
    def display(self)
        print("a reminder is set for " + self.date + " at " + self.time) #displays message

"""Adding Notes Manager"""
class NotesManager:
"""Initializing the class"""
    def __init__(self)
"""Manager Tasks"""
    def add_note(self) #adds a new note
    def delete_note(self, note_id) #deletes note with id = note_id)
        self.note_id = note_id #declears note id
    def show_notes(self) #show all notes
    def search_notes(self, "keyword") #search notes by keyword
