from django.shortcuts import render
from datetime import datetime
import random

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