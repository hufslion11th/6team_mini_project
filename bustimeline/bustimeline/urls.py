"""
URL configuration for bustimeline project.

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
from django.conf import settings
from django.conf.urls.static import static

from DownBus import views
from DownBus.views import mainPage
from DownBus.views import bus_list
from UpBus.views import bus_list_up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bus-list/', views.bus_list, name='bus_list'),
    path('', mainPage, name='main_page'),
    path('bus-list-up/', bus_list_up, name='bus_list_up'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

