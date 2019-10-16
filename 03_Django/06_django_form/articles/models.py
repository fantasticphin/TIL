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

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    class Meta:
        ordering = ['-pk',]
    # def __str__(self):
    #     return F'<Article({self.article_id}): Comment({self.pk} - {self.content})>'