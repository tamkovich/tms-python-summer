from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User


# def i(request):
#     user = User.objects.get(id=1)
#     user.w = '12'
#     print(user)
#     return HttpResponse(f'ABCDEFG {user.w}')
def log_in_out(self):
    if not self.user.is_authenticated:
        return HttpResponse(f"'<a href='/admin/logout'>Log in  {self.user}</a>'")
    user = self.user
    return HttpResponse(f"<a href='/admin/logout'>Logout from {user}</a>")

def greet(required):
    return render(required, '.blog.smth.html')

def dl(request):
    ur = User.object.get()