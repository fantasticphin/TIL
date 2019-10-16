from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles, }
    return render(request, 'articles/index.html', context)

def create(request):
    '''
    FORM Class
    1. 모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를 통해 데이터 정제 후 DB에 실제 저장하는 logic 필요
    
    Model Form
    1. 이미 모델에 대한 정보(필드, 스키마)를 알고 있기 때문에 어떤 모델에 레코드를 넣어야 하는지 알고 있음.
    2. Form.save()만 해도 DB에 저장됌

    '''
    if request.method == 'POST':
        # 폼 인스턴스 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            article = form.save() #form 이랑 model form 과의 차이
            # embed()
            # # form.cleaned.data 를 통해 폼 데이터를 정제한다(form.cleaned_data -> Dict)
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        # embed()
    context = {'form':form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save()
            return redirect('articles:detail', article.pk)
    else:
        comment_form = CommentForm()   
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        #instance -> 수정의 대상이 되는 특정한 글 객체
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            # embed()
            return redirect('articles:detail', article.pk)
    else: #get 요청
        form = ArticleForm(instance=article) #.__dict__)
        # embed()
    context = {'form':form, 'article': article, }
    return render(request, 'articles/form.html', context)

    '''
    CREATE * UPDATE 는 html 파일 공유

    create 로직
    1. get
    - 사용자가 데이터를 입력 할 수 있는  form 을 제공

    2. post
    - 사용자가 보낸 새로운 글을 DB에 저장

    update 로직
    1. get
    - 기존 사용자의 글이 입력된 form 제공, redirect 는 get 요청 // render는 내가 html 파일을 보겠다

    2. post
    - 수정된 글을 DB에 저장
    '''
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail', article.pk)


# def comments_delete(request, article_pk):
#     comment = get_object_or_404(Article, pk=article_pk)
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('articles:index')
#     return redirect('articles:detail', article.pk)