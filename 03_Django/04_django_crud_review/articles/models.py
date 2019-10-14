from django.db import models

class Article(models.Model): #Artcle 은 바로 엑셀의 시트 느낌이다
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self): #django orm 이 만들어준다
            return f'제목: {self.title}, 내용: {self.content}' #django가 생성해준 orm, field 를 정의해줌

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk', ]

    def __str__(self):
        # return f'댓글: {self.content}'
        return f'<Article({self.article_id}): Comment({self.pk} - {self.content})>'