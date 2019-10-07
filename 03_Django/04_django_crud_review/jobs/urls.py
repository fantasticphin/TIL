from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.index, name='index'), #GET 요청
    path('past_life/', views.past_life, name='past')
]