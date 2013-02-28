from django import forms


class InsertForm(forms.Form):
    table = forms.CharField()
    cvs = forms.FileField()
