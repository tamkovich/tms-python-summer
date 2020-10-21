from django.utils import http
from django.views.generic import ListView,\
                                 DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.urls import path
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from blog.models import Article
from profiles.models import Profile
from blog.forms import ArticleForm, CommentForm, UserForm
from django.http import request
from django.http import HttpResponseRedirect, response


class UserListView(ListView):
    model = User
    template_name = 'main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['users'] = self.object_list
        context['form'] = ArticleForm
        return context

    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace() #  дебаггер
        form = ArticleForm(request.POST)
        form.is_valid()
        form.save()
        return self.get(request, *args, **kwargs)

class UserDetailView(DetailView):
    model = User
    template_name = 'user.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users')

class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['articles'] = self.object_list
        context['form'] = ArticleForm
        return context

    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace() #  дебаггер
        form = ArticleForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return self.get(request, *args, **kwargs)


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'article.html'
    slug_field = 'title'
    slug_url_kwarg = 'title'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect('')


class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles')

class ProfileListView(ListView):
    model = User
    template_name = 'users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['users'] = self.object_list
        context['form'] = UserForm
        return context

    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace() #  дебаггер
        form = UserForm(request.POST, request.FILES)
        form.is_valid()
        form.save()
        return self.get(request, *args, **kwargs)



# class AvatarUpdate(UpdateView):
#     model = Profile
#     fields = ['avatar']
#     success_url = reverse_lazy('users')



# class ProfileDetailView(DetailView):
#     model = User
#
# class ProfileCreate(CreateView):
#     model = User
#     fields = ['email', 'username', 'first_name', 'last_name', 'avatar']
#     success_url = reverse_lazy('users')
#
#
# class ProfileUpdate(UpdateView):
#     model = Profile
#     fields = ['email', 'username', 'first_name', 'last_name', 'avatar']
#     success_url = reverse_lazy('users')
#     slug_field = 'user'
#     slug_url_kwarg = 'user'
#
# class ProfileDelete(DeleteView):
#     model = User
#     success_url = reverse_lazy('users')
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
#
# class ProfileDetailView(DetailView):
#     model = User
#
# class ProfileCreate(CreateView):
#     model = User
#     fields = ['email', 'username', 'first_name', 'last_name', 'avatar']
#     success_url = reverse_lazy('get-user')
#
# class ProfileUpdate(UpdateView):
#     model = User
#     fields = ['email', 'username', 'first_name', 'last_name', 'avatar']
#     success_url = reverse_lazy('get-user')
#
# class ProfileDelete(DeleteView):
#     model = User
#     success_url = reverse_lazy('get-user')
# class CommentDetailView(DetailView):
#     model = Comment
#     template_name = 'comment.html'
#     slug_field = 'article'
#     slug_url_kwarg = 'article'


# class CommentListView(ListView):
#     model = Comment
#     template_name = 'comments.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=None, **kwargs)
#         context['comments'] = self.object_list
#         context['form'] = CommentForm
#         return context
#
#     def post(self, request, *args, **kwargs):
#         # import pdb; pdb.set_trace() #  дебаггер
#         form = CommentForm(self.request.POST)
#         form.is_valid()
#         form.save()
#         return self.get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     # import pdb; pdb.set_trace() #  дебаггер
    #     form = CommentForm(request.POST)
    #     self.article = self.get_object()
    #     self.author = self.request.user
    #     form.is_valid()
    #     form.save()
    #     return self.get(request, *args, **kwargs)

# class CommentListView(ListView):
#     model = Comment
#     template_name = 'comments.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=None, **kwargs)
#         context['comments'] = self.object_list
#         context['form'] = CommentForm
#         return context
#
#     def post(self, request, *args, **kwargs):
#         # import pdb; pdb.set_trace() #  дебаггер
#         form = CommentForm(request.POST)
#         form.is_valid()
#         form.save()
#         return self.get(request, *args, **kwargs)


# def article(request):
#     articles = Article.objects.all()
#     return render(request, "articles.html", context={'title': 'Articles', 'articles': articles})

# class ArticleListView(ListView):
#     model = Article
#     template_name = 'articles.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=None, **kwargs)
#         context['articles'] = self.object_list
#         context['form'] = ArticleForm
#         return context
#
#     def post(self, request, *args, **kwargs):
#         # import pdb; pdb.set_trace() #  дебаггер
#         form = ArticleForm(request.POST)
#         form.is_valid()
#         form.save()
#         return self.get(request, *args, **kwargs)

# def home(request):
#     users = User.objects.all()
#     return render(request, "main.html", context={'users': users, 'form': ArticleForm()})

# def get_user(request, username):
#     return render(request, 'user.html', context={
#         'user': User.objects.get(username=username)
#     })
#

# def create_comment(request):
#     if request.POST:
#         Comment.object.create(
#             text=request.POST.get('text')
#         )
#     return render(request, 'create_comment.html')