from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class HomePageView(ListView):
    model=Post
    template_name='base.html'
    context_object_name= 'all_posts'



# Create your views here.
