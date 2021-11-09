""" Urls for shorturl app. """

from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('', views.url_shortener, name='index'),
    path('view-urls/', views.view_urls, name='view_urls'),
    path('<str:shortened_part>', views.view_shorturl, name='shorturl'),
]
