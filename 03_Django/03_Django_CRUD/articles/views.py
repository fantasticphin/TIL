from django.shortcuts import render, redirect #redirect 는 페이지를 계속 보여주지 않고, 이전 페이지로 바로 돌아가게 한다.
from .models import Article # 현재 디렉토리 모델 파일에서 Article 속성을 불러올 수 있도록 한다.

def index(request): # 모든 글들이 존재하는 페이지
    articles = Article.objects.order_by('-id')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title') #new.html 에서 form action 의 쏘는 박스가 사라지면, print 를 통해 확인해보자
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect (f'/articles/{article.pk}/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render (request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk) #기존 글을 떙겨오는 역할
    article.title = request.POST.get('title') #수정 값이 들어있는 박스
    article.content = request.POST.get('content')
    article.save()

    return redirect(f'/articles/{article.pk}/') #수정한 글이 제대로 보이는지 확인하는 절차!