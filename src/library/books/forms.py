from django.forms import ModelForm

from .models import Books


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author_name', 'description']