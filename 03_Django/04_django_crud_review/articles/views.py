from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def new(request): #사용자가 글을 입력할 수 있도록 도와주는 함수
    return render(request, 'articles/new.html')

def create(request): #new 와 달리 사용자가 상호작용
    title = request.POST.get('title') #quarry dictionary 형태임
    # print(title)
    content = request.POST.get('content')
    
    # #1. 첫번쨰 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # #2 두번째 방법
    # article = Article(title =title, content=content)
    # article.save()

    #3 세번쨰 방법, save method 불필요
    Article.objects.create(title=title, content=content)
    
    return redirect('/articles/')

def detail(request, pk):
    pass