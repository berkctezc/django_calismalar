from django.shortcuts import render
from django.views.generic import TemplateView


# göstermek istediğimiz template'i belirtmek
class HomePageView(TemplateView):
    template_name = 'index.html'