import webbrowser

#webbrowser.open('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=ssafy')
#pythwebbrowser.open_new('https://google.com')
#webbrowser.open_new_tab('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=ssafy')

#idol = ['전효성', '조이', '채연', 'SES']
#for i in idol:
#    webbrowser.open('https://search.naver.com/search.naver?query={}'.format(i))

idols = ['BTS', 'Secret', 'Winner', '코미디빅리그']
for idol in idols:
    print(type(idol))
    webbrowser.open('https://search.naver.com/search.naver?query='+idol)