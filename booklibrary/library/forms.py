from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True, error_messages={'required': 'Please enter a title.'})
    author = forms.CharField(max_length=100, required=True, error_messages={'required': 'Please enter an author.'})
    published_date = forms.DateField(required=True, error_messages={'required': 'Please enter a published date.'})
    description = forms.CharField(required=False)
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description']
