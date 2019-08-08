from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)#맥스렌스 설정필요
    content = models.TextField()#글자제한 없음
    created_at = models.DateTimeField(auto_now_add=True) #만들어진 시간..
    updated_at = models.DateTimeField(auto_now=True) #매번 업데이트 될 때 마다..

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'