"""Forms of the project."""
from django import forms
# Create your forms here.

class MyForm(forms.Form):
    # Example fields
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Email Address')
    age = forms.IntegerField(label='Age')
    comment = forms.CharField(widget=forms.Textarea, required=False)
