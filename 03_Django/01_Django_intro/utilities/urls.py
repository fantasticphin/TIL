from django.urls import path
from . import views # (.) 을 이용해 같은 디렉토리에 있는 위치를 불러온다

urlpatterns = [
    path('', views.index),#index는 빈 칸으로 내비두고 /를 하지 않아도 됌
    path('mamago/', views.mamago),
    path('translated/', views.translated),
]