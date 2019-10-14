from django.shortcuts import render, redirect
from .models import Job
from faker import Faker
from decouple import config
import requests
from pprint import pprint

def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    name = request.POST.get('name')
    person = Job.objects.filter(name=name).first() #filter 함수는 값이 없어도 에러가 나지 않음, get 은 에러가 날 수 있음
    #DB에 이름이 있을 경우
    if person:
        past_job = person.past_job
    #DB에 이름이 없을 경우
    else:
        fake = Faker()
        #랜덤 직업 생성
        past_job = fake.job()
        # 새로운 이름, 직업 추가 후 DB 저장
    person = Job(name=name, past_job=past_job)
    person.save()
    #GIPHY
    #1. API KEY 가져오기
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    #2. 요청 URL 셋팅
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    #3. 실제 요청 보내자. 
    data = requests.get(url).json() #json 파일은 딕셔너리 형태와 유사
    #4. image 추출
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None
    
    # NAVER IMAGE
    NAVER_ID = config('NAVER_ID')
    NAVER_SECRET = config('NAVER_SECRET')

    headers = {
        'X-Naver-Client-Id': NAVER_ID,
        'X-Naver-Client-Secret': NAVER_SECRET
    }

    #2. 요청 URL 준비
    naver_url = f'https://openapi.naver.com/v1/search/image?query={past_job}&filter=medium&display=1'

    #3. 실제 요청 보내기
    naver_data = requests.get(naver_url, headers=headers).json()
    pprint(naver_data)

    #4.
    naver_image = naver_data.get('items')[0].get('link')
      
    context = {'person':person, 'image':image, 'naver_image':naver_image}
    
    return render(request, 'jobs/past_life.html', context)