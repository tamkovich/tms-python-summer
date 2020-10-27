from blog.models import Article, Film, User, Comment
from profiles.models import Profile
from django import forms


class ArticleForm(forms.ModelForm):
    description = forms.CharField(label='Oписание')
    forms.TextInput
    class Meta:


        model = Article
        fields = ['title', 'description', 'image']


class Userform(forms.ModelForm):
    username = forms.CharField(label='Oписание')
    # forms.TextInput

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'username': forms.TextInput(attrs={
            'placeholder': "Enter the username"
        }),
            'password': forms.TextInput(attrs={
                'placeholder': "Enter the password"
        })
        }



class FilmForm(forms.ModelForm):
    description = forms.CharField(label='FILM:')
    forms.TextInput
    class Meta2:

        model = Film
        fields = ['name', 'rating']



class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label='descrip')
    forms.TextInput
    class Meta:

        model = Comment
        fields = ['comment_text']


class ProfileForm(forms.ModelForm):
    avatar = forms.CharField(label='descrip')
    forms.FileInput

    class Meta:
        model = Profile
        fields = ['avatar']