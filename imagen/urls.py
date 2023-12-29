from django.urls import path
from .views import index, eliminar
urlpatterns = [
    path('', index , name='index'),
    path('eliminar/<int:idimagen>/' , eliminar ,name='eliminar'),
]
