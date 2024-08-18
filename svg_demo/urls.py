from django.urls import path
from . import views

app_name = "svg_demo"
urlpatterns = [
    path('', views.index, name='index'),
    path('r', views.roti, name='roti'),
]