from django.urls import path
from . import views
####
#from django.conf import settings
#from django.conf.urls.static import static 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('postb', views.post_postb, name='post_postb'),
    path('postc', views.post_postc, name='post_postc'),
    path('postd', views.post_postd, name='post_postd'),
    path('about', views.about, name='about'),
    path('contacto', views.contacto, name='contacto'),

    
]
