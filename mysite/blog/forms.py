from django import forms

from blog.models import Article, Comment

class ArticleForm(forms.ModelForm):

    description = forms.CharField(
        label='Описание'
    )

    class Meta:
        model = Article
        fields = 'title', 'description', 'author', 'image'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'name', 'email', 'body'


