from django.urls import path
from . import views

urlpatterns = [
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('pong/', views.pong),
    path('ping/', views.ping),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('lotto/', views.lotto),
    path('ispal/<word>/', views.ispal),
    path('isbirth/', views.isbirth),
    path('STUdent/<name>/', views.STUdent),
    path('info/', views.info),
    path('template_language/', views.template_language),
    path('area_circle/<int:r>/', views.area_circle), #요청페이지 이름/변수/ 중앙관리자를 통해 부르는 함수
    path('multi/<int:ran>/<int:ran2>/', views.multi),
    path('introduce2/<name>/<int:age>', views.introduce2),
    path('hello/<name>/<int:age>/', views.hello),
    path('lorempic/', views.lorempic),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
    ]