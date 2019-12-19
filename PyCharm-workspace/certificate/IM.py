# import sys
# sys.stdin = open('IM.txt')
#
# for tc in range(1, int(input()) + 1):
#     B = int(input())
#     table = [list(map(int, input().split())) for _ in range(B)]
#     winner = 0
#     cnt = 0
#     for i in range(B):
#         for j in range(B):
#             cnt = 0
#             for a in range(i + 1):
#                 for b in range(j + 1):
#                     if table[a][b] == 1:
#                         cnt += 1
#                     elif table[a][b] == 2:
#                         cnt += 0
#                     else:
#                         cnt += 0
#
#             for c in range(i + 1, B):
#                 for d in range(j + 1):
#                     if table[d][c] == 1:
#                         cnt += 1
#                     elif table[d][c] == 2:
#                         cnt += 0
#                     else:
#                         cnt += 0
#
#             for e in range(i + 1):
#                 for f in range(j + 1, B):
#                     if table[f][e] == 1:
#                         cnt += 1
#                     elif table[f][e] == 2:
#                         cnt += 0
#                     else:
#                         cnt += 0
#
#             for g in range(i + 1, B):
#                 for h in range(j + 1, B):
#                     if table[g][h] == 1:
#                         cnt += 1
#                     elif table[g][h] == 2:
#                         cnt += 0
#                     else:
#                         cnt += 0
#
#             for dx in range(B):
#                 for dy in range(B):
#                     if table[dx] == table[dy] and table[dx][dy] == 1:
#                         cnt += 1
#                     elif table[dx] == table[dy] and table[dx][dy] == 2:
#                         cnt += 0
#                     else:
#                         cnt += 0
#
#             # for cx in range(B - 1, -1, -1):
#             #     for cy in range(B):
#             #         if table[cy] == [cx] and table[cy][cx] == 1:
#             #             cnt += 1
#             #         elif table[cy][cx] == 1:
#             #             cnt += 1
#             #         else:
#             #             cnt += 0
#
#     if cnt == 5:
#         winner = 1
#     else:
#         winner = 2
#     print('#{} {}'.format(tc, winner))

# e, f, c = map(int, input().split())
# s = e + f
# i = 0
# while s >= c:
#     i += s // c
#     s = s //c + s % c
# print(i)

for tc in range(1, int(input())+1):
   N = int(input())  #박스 갯수 정해주는 정수
   cnt = 0 #겹치는 부분을 체크하는 반복수
   sol=[['0']*10 for _ in range(10)] #게임판, str 으로 넣어 추후에 추출하기 편함
   data= [[0]*5for _ in range(N)] #박스 좌표와 색상 /// 정수로 받음
   for i in range(N):
       data[i] = list(map(int,input().split()))
   for i in range(N):
       for j in range(data[i][0],data[i][2]+1):
           for k in range(data[i][1],data[i][3]+1):
               sol[j][k] +=str(data[i][4])
   for i in range(10):
       for j in range(10):  # 전체 배열을 돌면서 중복되는 부분을 체크 후 cnt 에 추가
           if '1' in sol[i][j] and '2' in sol[i][j]:
               cnt+=1
   print("#{} {}".format(tc,cnt))
