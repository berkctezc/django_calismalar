from django.urls import path
from .views import BlogPageView, BlogDetailView
# from .views import HomePageView #blog.views fakat aynı directoryde oldugumuz icin bos birakabiliriz

# ana projeden bu urls'e yönlendirildik buradan da views.py 'ye
urlpatterns = [
    #path('directory', CagirilacakView)
    path('', BlogPageView.as_view(), name='index'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'), #pk=primary key
]


'''
urlpatterns = [
    #path('directory', CagirilacakView)
    path('', HomePageView.as_view(), name='index'),

]
'''
