from django.urls import path
from .views import HomePageView #blog.views fakat aynı directoryde oldugumuz icin bos birakabiliriz

#ana projeden bu urls'e yönlendirildik buradan da views.py 'ye
urlpatterns = [
    #path('directory', CagirilacakView)
    path('', HomePageView.as_view(), name='index'),

]