from django.http import HttpResponse
from django.contrib.auth.models import User

def hello(request):
    user = request.user
    import pdb;
    return HttpResponse(f"hello {user.first_name}")
