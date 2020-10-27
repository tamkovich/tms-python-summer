from django.shortcuts import render, redirect
from blog.forms import ArticleForm, FilmForm, Userform
from django.views.generic import ListView, DetailView, DeleteView

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from .models import Article, Film, Danger, Member



def test(request):
    print(request.GET.get)
    if request.POST:
        form = ArticleForm(request.POST)
        form.is_valid()
        form.save()
        # Article.objects.create(
        #     title=form.title,
        #     description=form.description,
        # )
    return render(request, 'create_article.html', context={'form': ArticleForm()})


def usermodel(request):
    if request.POST:
        form1 = Userform
        form1.is_valid()
        form1.save()
    return render(request, 'create_user.html', context={'form1': Userform})

def get_user(request, username):
    return render(request, 'user.html', context={'user': User.objects.get(username=username)})
    # return HttpResponse(username)

def way(request):

    return redirect('/')

def func(request):
    article_objects = Article.objects.all()
    template = loader.get_template('smth.html')
    context = {'articles': article_objects}
    return HttpResponse(template.render(context, request))


def home(request):
    if not request.user.is_authenticated:
        return redirect('admin/login/')
    else:
        users = User.objects.all()
        tmp = loader.get_template('work.html')
        context2 = {'users': users, 'form': ArticleForm()}
        return HttpResponse(tmp.render(context2, request))


def arcti(request):
    artics = Article.objects.all()
    x = loader.get_template('arts.html')
    contains_of = {'arts': artics}
    return HttpResponse(x.render(contains_of, request))






class UserListView(ListView):
    model = User
    template_name = 'work.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contextt = super(UserListView, self).get_context_data(object_list=None, **kwargs)
        contextt['users'] = self.object_list
        contextt['form'] = ArticleForm
        return contextt

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST, request.FILES or None)
        form.is_valid()
        form.save()
        return self.get(request, *args, **kwargs)

class UserDetailView(DetailView):
    model = User
    template_name = 'smth.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

class UserDeleteView(DeleteView):
    model = User
    success_url = '/'
    template_name = 'delete_user.html'



def retur(request):
    dangers = Danger.objects.all()
    consists = {'dangers': dangers}
    return render(request, 'danger.html', consists)

class FilmDetailView(DetailView):
    model = Film
    template_name = 'movie.html'
    slug_field = 'name'
    slug_url_kwarg = 'description'


def film_maker(request):
    all_films = Film.objects.all()
    some_tmp = loader.get_template('film_html.html')
    content = {'all_films': all_films, 'form2': FilmForm()}
    return HttpResponse(some_tmp.render(content, request))


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'


class DangerDetailView(DetailView):
    model = Danger
    template_name = 'dang_get.html'
    slug_field = 'name'
    slug_url_kwarg = 'name'


def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)


def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')


def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)


def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/')


def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/')


def goto(request):
    return redirect('admin/auth/user/add/')

def link_to(request, pk):

    return render(request, context={'pk': User.objects.get(pk=pk)})
    # return redirect('admin/auth/user/<pk>/change/')


