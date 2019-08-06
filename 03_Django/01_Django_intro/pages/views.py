from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def lorempic(request):
    return render(request, 'lorempic.html')

#2. Tmplate Variable(템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {'pick':pick}
    return render(request, 'dinner.html', context) #context 가 들어가는 자리는 딕셔너리가 들어가는 자리이다

#3. Variable Routing(동적 라우팅)
def hello(request, name, age):
    
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name, 
        'age': age, 
        'pick' : pick
        }
    return render(request, 'hello.html', context)

    #4. 실습
    #4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기소개 페이지
    # 함수 정의 후 괄호 안에 직접적으로 이름을 적으면 주소창에도 입력해야 올바르게 실행이 됌
def introduce2(request, name, age):    
    name = ['Zzulu', 'Jasmine', 'Aladin']
    age = [19, 20, 21]
    pick = random.choice(name)
    pick2 = random.choice(age)
    context = {
        'name': name,
        'age': age,
        'pick': pick,
        'pick2': pick2,
    }
    return render(request, 'introduce2.html', context)
    #4-2. 두개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력

def multi(request, ran, ran2):

    context = {
        'ran': ran,
        'ran2': ran2,
        'ran3': ran * ran2
    }
    return render(request, 'multi.html', context)

    #4-3 반지름을 인자로 받아 원의 넓이를 구하시오

def area_circle (request, r):
    r1 = 3.14 * r**2
    context = {'r1': r1,}
    return render(request, 'area_circle.html', context)

 #5 DTL(Django Template Language)
def template_language(request):
    menus = ["짜장면", "양장피", "탕수육", "짬뽕"]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)

# 6. homeworkshop
def info(request):
    #함수 옆에 특정 값을 적지 않으면 , 바로 context<딕셔너리>에 기입한다
    Teacher = 'NAME'
    student = ['홍길동', '박길동', '김길동']
    
    context = {
        'Teacher': Teacher,
        'student': student,
    }
    return render(request, 'info.html', context)

def STUdent(request, name):
    age = [17, 18, 19]
    pick = random.choice(age)

    context = {
        'name': name,
        'pick': pick,
    }
    return render(request, 'STUdent.html', context)

    #6.실습
    #6-1. isbirth
def isbirth(request):
    today = datetime.now()
    
    if today.month == 4 and today.day == 7:
        result = True
    else:
        result = False
    context = {
        'result': result,
    }
    return render(request, 'isbirth.html', context)

    #6-2 회문인지 판단
def ispal(request, word):
    result = False
    if word == word[::-1]:
        result = True
    
    context = {
       'word': word,
       'result': result,
    }
    return render(request, 'ispal.html', context)

    #6-3 로또 번호 추첨
def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos = list(random.sample(range(1,46), 6))

    context = {
        'real_lottos': real_lottos,
        'lottos': lottos,
    }
    return render(request, 'lotto.html', context)

#7. Form - GET 요청
def throw(request):    
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message': message,
        'message2': message2, #html 파일에서 볼 수 있게 딕셔너리 형태로 쓴다!!
    }
    return render(request, 'catch.html', context)

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'pong.html', context)

#8. FORM - GET 실습 (아스키 아티)
def art(request): #던져줄 함수는 html 에 띄어주는 역할
    return render(request, 'art.html')

def result(request):
    #art 에 속한 html의 form 에서 날린 데이터를 받는다
    funart = request.GET.get('funart')
    #2. ASCII ART api 로 요청을 보내 응답 결과를 fonts 에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    #fonts(str)를 font(list)로 바꾼다.
    fonts = fonts.split('\n')
    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font 라는 변수에 저장(str)
    font = random.choice(fonts)
    #5. 위에서 사용자에게 받은 funart 와 font를 가지고 다시 요청을 보낸다. 그리고 응답 결과를 result 에 저장.
    result = requests.get(f'http://artii.herokuapp.com/make?text={funart}&font={font}').text

    context = {
        'result':result
    }
    return render(request, 'result.html', context)

#9. FORM - POST
def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'password': pwd, #'변수' 는 html 에서 사용될 변수
    }
    return render(request, 'user_create.html', context)