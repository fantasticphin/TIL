from django.db import models #models 에 클래스를 만듬, 이쁘게 보이도록 __str__ 도 만들어줌

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField (auto_now = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
            return f'{self.id}번글 - {self.title}: {self.content}'