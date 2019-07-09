import requests
from bs4 import BeautifulSoup
#url 변수를 생성하여 코딩을 간단하게
url = 'https://finance.naver.com/sise/'
#html 변수를 생성하여 코딩을 간단하게
html = requests.get(url).text
print(type(html))
soup = BeautifulSoup(html, 'html.parser')
kospi = soup.select_one('#KOSPI_now').text
print(f'오늘의 코스피 지수는 {kospi} 입니다.')