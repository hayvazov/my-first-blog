from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('limpieza-de-sofas/', views.limpieza_de_sofas, name='limpieza_de_sofas'),
]


