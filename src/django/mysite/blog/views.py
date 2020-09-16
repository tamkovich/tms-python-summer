from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from .models import Article

def test(request):
    return HttpResponse('AAAAAAAAAAA')




def get_user(request, username):
    return render(request, 'user.html', context={'user': User.objects.get(username=username)})
    # return HttpResponse(username)


def func(request):
    article_objects = Article.objects.all()
    template = loader.get_template('smth.html')
    context = {'articles': article_objects}
    return HttpResponse(template.render(context, request))

def home(request):
    users = User.objects.all()
    tmp = loader.get_template('work.html')
    context2 = {'users': users}
    return HttpResponse(tmp.render(context2, request))
