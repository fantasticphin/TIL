"""
python dictionary 문제
"""

#1. 평균을 구하세요
# score = {
#     '수학':80,
#     '국어':90,
#     '음악':100
# }

# ts=0
# for t in score.values():
#     ts += t
# print(ts)
# avs = ts/len(score)
# print(avs)

#2. 반 평균을 구하자
# score = {
#     'a': {
#     '수학':80,
#     '국어':90,
#     '음악':100
#     },
#     'b': {
#     '수학':80,
#     '국어':90,
#     '음악':100
#     }
# }
# total_score=0
# length=0

# for person_score in score.values():
#     for subject_score in person_score.values():
#         total_score += subject_score
#         length += 1

# average_score = total_score / length
# print(average_score)

#3.도시별 최근 3일 온도입니다. 
#3-1. 각 도시별 최근 3일의 온도 평균과 도시 중 최근 3일 중 가장 더운 곳은?
#3-2. 서울은 영상 2도 였던 적이 있나요? -> ex. 네 있어요! or 없어요

city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 9],
    '부산': [2, -2, 9]
}
for name, temp in city.items():
    avg_tmp = sum(temp) / len(temp)
    print(f'{name} : {avg_tmp}')
print(2 in city['서울'])