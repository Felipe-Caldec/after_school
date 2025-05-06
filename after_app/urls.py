from django.urls import path
from after_app.views import portada, talleres, galeria

urlpatterns = [
    path('', portada, name='portada'),
    path('talleres/', talleres, name='talleres'),
    path('galeria/', galeria, name='galeria'),
]