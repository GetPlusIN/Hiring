from django import forms
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'published_date')
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }

    #This is used for crispy forms
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
