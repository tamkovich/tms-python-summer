from django.http import HttpResponse
from django.contrib.auth.models import User  # обращение к таблице с юзерами

# def hello(request):
#     user = User.objects.get(id=2)  # запрос на конкретного пользователя с id=1
#     user.first_name = "Gosha"
#     user.save()
#     print(user)
#     return HttpResponse(f'Hello, {user.get_username()} {user.first_name}!')

# def hello(request):
#     user = request.user  # запрос для отображения пользователя, который сейчас залогинен на сайте
#     return HttpResponse(f'Hello, {user.get_username()} {user.first_name}!')

# def hello(request):
#     if not request.user.is_authenticated:
#         return HttpResponse('Go away!')  # для того, если никто не залогинился
#     return HttpResponse(f'Hello, {request.user}!'

def start(request):
    if not request.user.is_authenticated:
        return HttpResponse(f"<p>START</p>"
                            f"<a href='/admin/login'>Login from {request.user}</a>")  # для того, если никто не залогинился
    return HttpResponse(f"<a href='/admin/logout'>Logout from {request.user}</a>")

