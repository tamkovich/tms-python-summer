from django import forms

from .models import Book

class BookForm(forms.ModelForm):

    description = forms.CharField(
        label='Описание'
    )

    class Meta:
        model = Book
        fields = 'title', 'description', 'author',
