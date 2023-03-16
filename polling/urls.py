from django.urls import path, include
from . import views

app_name = 'polling'

urlpatterns = [
    path('polling', views.polling_view, name='polling'),
    path('polling/result', views.result_view, name='result'),
]