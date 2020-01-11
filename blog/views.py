from django.shortcuts import render
#from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Post


class BlogPageView(ListView):
    model = Post
    template_name = 'index.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'


'''
# göstermek istediğimiz template'i belirtmek
class HomePageView(TemplateView):
    template_name = 'index.html'
'''
