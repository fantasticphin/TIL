from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail), # article / 숫자를 넣으면 views 의 deatil 로 넘어가게 됌 // url 경로로 들어왔을 떄 변수 이름을 생성하면, views 에서도 동일한 이름으로 전달받음
    path('<int:pk>/delete/', views.delete),
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]