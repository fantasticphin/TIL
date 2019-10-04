from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), # article / 숫자를 넣으면 views 의 deatil 로 넘어가게 됌 // url 경로로 들어왔을 떄 변수 이름을 생성하면, views 에서도 동일한 이름으로 전달받음
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]