from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Yeah, It is my first app and it is Working.")

# Create your views here.
def post_list(request):
    return render(request, 'post.html')

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'