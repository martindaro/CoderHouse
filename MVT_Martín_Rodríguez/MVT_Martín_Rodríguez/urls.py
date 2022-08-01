"""MVT_Martín_Rodríguez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom import INDEX_SIZE_ERR
from django.contrib import admin
from django.urls import path
from MVT_app.views import MVT_Portada
from MVT_app.views import lista_familias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familias/', lista_familias),
    path('portada/', MVT_Portada),
    #path('', index_MVT)

]

