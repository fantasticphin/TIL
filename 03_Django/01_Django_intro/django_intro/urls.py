"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from pages import views

urlpatterns = [
    path('utilities/', include('utilities.urls')), #django intro urls는 문지기 역할, 1차로 여기서 확인하고, utility 확인후, 해당 app 으로 전송시켜줌
    path('pages/', include('pages.urls')), #pages 로 들어오는 요청의 나머지 뒷부분은 모두 pages.urls 에서 확인한다
    path('admin/', admin.site.urls),
] #이 화면이 순정입니다. 초창기 화면
