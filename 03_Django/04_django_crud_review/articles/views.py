from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Article
from IPython import embed

# def create(request):
#     try:
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         article = Article(title=title, content=content)
#         article.full.clean() #유효성 검사
#     except ValidationError:
#         raise ValidationError('Your Error Message')
#     else:
#         article.save()
#         return redirect(f'/articles/{article.pk}/')

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# def new(request): #사용자가 글을 입력할 수 있도록 도와주는 함수
#     embed()
#     return render(request, 'articles/new.html')

def create(request): #new 와 달리 사용자가 상호작용
    # POST 요청일 떄
    if request.method == 'POST':
        title = request.POST.get('title') #quarry dictionary 형태임
        content = request.POST.get('content')
        article = Article(title =title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    # GET 요청일 때
    else:
        return render(request, 'articles/create.html')
    # #1. 첫번쨰 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # #2 두번째 방법
    # article = Article(title =title, content=content)
    # article.save()

    #3 세번쨰 방법, save method 불필요
    # Article.objects.create(title=title, content=content)
    
    # return redirect('articles:detail', article.pk) #원래는 return render 이지만 redirect 함수를 적용한 이유는 '되돌아 가거나' get or post 요쳥에 따라 redirect 변경됌

def detail(request, pk): #pk 는 특정 글 하나를 잡아서 보여줘야 해서 pk 라는 인식표가 필요함
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }

    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article':article,
#     }

#     return render (request, 'articles/edit.html', context)

def update(request, pk):
    # embed()
    article = Article.objects.get(pk=pk) #query set 를 챙겨온다, pk 의 글이 담겨있음
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article':article}
        return render (request, 'articles/update.html', context)