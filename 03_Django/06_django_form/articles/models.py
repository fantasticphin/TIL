from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',) #tuple 형태 꼮!!! 콤마를 찍어줘야함~~!!!!

    def __str__(self):
        return self.title