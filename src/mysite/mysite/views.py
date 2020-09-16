from django.http import HttpResponse
from django.contrib.auth.models import User


def hello(request):
    if not request.user.is_authenticated:
        return HttpResponse("Go away")
    return HttpResponse(f"<a href='/admin/logout'>Logout from {request.user}</a>")
