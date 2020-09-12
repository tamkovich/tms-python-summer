from .models import Books
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author_name', 'description']