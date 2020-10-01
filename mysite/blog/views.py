from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.contrib.auth.models import User
from blog.models import Article
from blog.forms import ArticleForm


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

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    slug_field = 'title'
    slug_url_kwarg = 'title'


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
        form = ArticleForm(request.POST)
        form.is_valid()
        form.save()
        return self.get(request, *args, **kwargs)


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

# def create(request):
#     print('----------------------')
#     print(request.POST.get("title"))
#     print(request.POST.get("description"))
#     print('----------------------')
#     if request.POST:
#         form = ArticleForm(request.POST)
#         print('-------------')
#         print(form.is_valid())
#         print('-------------')
#         form.save()
#     return render(request,
#                   'create_article.html',
#                   context={'form': ArticleForm()}
#                   )
