from django.urls import path #path 를 불러와 아래에서 사용가능하게 만든다
from . import views

urlpatterns = [
    path('', views.index), #'' 로 시작하지면 기본, 혹은 메인페이지 이다
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete/', views.delete),
]