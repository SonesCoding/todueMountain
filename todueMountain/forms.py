from django import forms
from .models import tdTask, User, journalEntry

class TaskForm(forms.ModelForm):
        class Meta:
            model = tdTask
            fields = ['TaskTitle','TaskDescr']
        
        
class EntryForm(forms.ModelForm):
        class Meta:
            model = journalEntry
            fields = ['EntryTitle','mood','entryText']