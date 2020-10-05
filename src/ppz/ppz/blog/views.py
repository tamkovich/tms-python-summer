from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from blog.forms import ArticleForm
from blog.forms import BookForm
from blog.models import Article
from blog.models import Book


class UserListView(ListView):
    model = User
    template_name = 'main.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['users'] = self.object_list
        context['form'] = ArticleForm
        return context

    def post(self, request, *args, **kwargs):
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

class BookDetailView(DetailView):
    model = Book
    template_name = 'article.html'







