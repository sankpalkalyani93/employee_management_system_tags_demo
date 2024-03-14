from django import forms

class TagForm(forms.Form):
    tags = forms.CharField(max_length=100)