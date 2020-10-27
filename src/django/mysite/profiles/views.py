from django.shortcuts import render, HttpResponse
import blog.templates
from django.template import loader
# Create your views here.
from .models import Profile
from blog.forms import ProfileForm


def get_profiles(request):
    all = Profile.objects.all
    tmp3 = loader.get_template('profiles.html')
    sec = {'all': all, 'form2' : ProfileForm}
    return HttpResponse(tmp3.render(sec, request))