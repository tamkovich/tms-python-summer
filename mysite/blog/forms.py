from django import forms

from blog.models import Article

class ArticleForm(forms.ModelForm):

    description = forms.CharField(
        label='Описание'
    )

    class Meta:
        model = Article
        fields = 'title', 'description', 'author'
