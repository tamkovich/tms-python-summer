from django import forms

from blog.models import Article
from blog.models import Book

class ArticleForm(forms.ModelForm):

    description = forms.CharField(
        label='Описание'
    )

    class Meta:
        model = Article
        fields = ('title', 'description', 'author')

class BookForm(forms.ModelForm):

    description = forms.CharField(
        label='Описание'
    )

    class Meta:
        model = Book
        fields = ('title', 'description', 'author')