from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User

from blog.models import Article


def test(request):
    return HttpResponse("Test urls work cool")


def home(request):
    users = User.objects.all()
    return render(request, 'main.html', context={'users': users})


def get_user(request, username):
    return render(request, 'user.html', context={
        'user': User.objects.get(username=username)
    })


def create(request):
    if request.POST:
        Article.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
    return render(request, 'create_article.html')
