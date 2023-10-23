from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.practica, name='practica'),
    path('base',  views.base, name='base'),
    path('crear',views.create, name='crear' ),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar')
] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)