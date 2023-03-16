from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('logout/', views.logout_view, name='logout'),
]