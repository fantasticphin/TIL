# 1. Dictionary 만들기
lunch ={
    '중국집' : '02'
}
# 2. Dictionary 추가하기
lunch = dict(중국집='02')
# print(lunch)

lunch['분식집'] = '031'
# print(lunch)


# idol = {
#     'bts' : {
#         '지민': 24,
#         'RM': 25
#     }
# }
# 3.Dictionary value 가져오기
# print(idol['bts']['RM'])
# print(idol.get('bts').get('RM'))

#4. Dictionary 반복문 활용하기
#4-1. 기본활용
# for key in lunch:
#     print(key)
#     print(lunch[key])

#4-2. .items() - key, value 모두 가져오기
# for key, value in lunch.items():
#     print(key,value)

# #4-3. .values() -value만 가져오기
# for lunch in lunch.values():
#     print(value)

for key in lunch.keys():
    print(key)
