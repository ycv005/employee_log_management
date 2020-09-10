from django import forms


class EntryForm(forms.Form):
    """
    Form for the Entry
    """
    fields = '__all__'
