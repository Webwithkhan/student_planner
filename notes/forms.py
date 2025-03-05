from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["task", "title", "content"]
        widgets = {
            "task": forms.Select(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 mb-4 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white",
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 mb-4 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:text-white",
                    "placeholder": "Enter note title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "block p-2.5 w-full text-sm text-gray-900 mb-6 bg-gray-50 rounded-lg border border-gray-300 focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white",
                    "placeholder": "Write your note here...",
                    "rows": 4,
                }
            ),
        }
