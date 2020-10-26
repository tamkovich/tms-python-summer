from django import forms
from django.forms import Textarea
from blog.models import Article, Comment, User
from profiles.models import Profile
from django.shortcuts import render, redirect, get_object_or_404


class ArticleForm(forms.ModelForm):

    # description = forms.CharField(
    #     label='Описание'
    # )

    class Meta:
        model = Article
        fields = 'title', 'description', 'category', 'author', 'image',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def article_create(request, template_name='blog/create_article.html'):
        form = ArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, template_name, {'form': form})

    def article_update(request, pk, template_name='blog/article_form.html'):
        article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, template_name, {'form': form})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = 'text', 'author',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = 'username', 'first_name', 'last_name', 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def user_update(request, pk, template_name='auth/user_form.html'):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, template_name, {'form': form})

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = 'user', 'info', 'avatar',

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def profile_create(request, template_name='profiles/profile_create.html'):
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, template_name, {'form': form})

    def profile_update(request, pk, template_name='profiles/profile_form.html'):
        profile = get_object_or_404(Profile, pk=pk)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users')
        return render(request, template_name, {'form': form})





