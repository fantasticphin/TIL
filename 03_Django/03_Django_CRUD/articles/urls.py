from django.urls import path #path 를 불러와 아래에서 사용가능하게 만든다 #crud의 urls 파일에서 검문 후 여기로 넘어온다.
from . import views

urlpatterns = [
    path('', views.index), #'' 로 시작하지면 기본, 혹은 메인페이지 이다, 이 경우에 모든 글을 보여준다
    path('new/', views.new), # 글을 쓰는 것
    path('create/', views.create), #글을 쓰는 것임, 행 하나에 글을 삽입
    path('<int:pk>/', views.detail), #특정 글을 불러오기 때문에, 고유 번호를 식별해 뽑아와줌
    path('<int:pk>/delete/', views.delete), #특정 글을 삭제하기 때문에 전부 불러올 수 없다. 그러니 고유 식별 번호가 필요 & MUST!!!!, UPDATE 도 마찬가지!!
    path('<int:pk>/edit/', views.edit), #특정 글을 수정하기 때문에 전부 불러올 수 없다. 고로 pk 로 수식을 해 줌
    path('<int:pk>/update/', views.update),
]