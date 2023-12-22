"""
URL configuration for ruth_morales_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from seminario_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    #Formulario Agregar participantes e instituciones
    path('inscribirParticipante/', views.inscribir),
    path('agregarInstitucion/', views.agregarInstitucion),

    #Api Rest para los datos del Auto
    path('autor/', views.autor),

    # Class Based Views para el Modelo Inscritos
    path('inscritos/', views.InscritosList_class.as_view()),
    path('inscritos/<int:id>', views.InscritosDetalle_class.as_view()),

    #Función Based Views para modelo institución
    path('institucion/', views.institucion_list),
    path('institucion/<int:id>', views.institucion_detalle),
]
