from django.contrib import admin #crud 밑에 위치한 urls 는 검문소 역할, 여러 app 이 생성되었을 때 혼동을 막아줌, 각기 필요한 경로로 뿌려준다
from django.urls import path, include #include 함수를 통해 들어온 요청을 올바른 곳으로 전송해줌
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
]
# 파일이 업로드 된 이후에 프로젝트 내부에 존재하는 파일의 주소를 만들어 줌
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)