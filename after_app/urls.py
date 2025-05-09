from django.urls import path
from after_app.views import portada, talleres, galeria, quienes_somos

urlpatterns = [
    path('', portada, name='portada'),
    path('talleres/', talleres, name='talleres'),
    path('galeria/', galeria, name='galeria'),
    path('quienes_somos/', quienes_somos, name='quienes-somos'),
]