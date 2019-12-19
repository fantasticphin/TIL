# def fibs(num):
#     a, b = 0, 1
#     for i in range(num):
#         a, b = b, a + b
#     return a
#
# print(fibs(10))
#
# # P = int(input())
# # table = [[0]*3 for _ in range(3)]
# # new = [list(map(int, input().split())) for _ in range(9)]
# # for n in range(9):
# #     y = new[n][0]
# #     x = new[n][1]
# #     if n % 2 != 0:
# #         table[y-1][x-1] = 'X'
# #     else:
# #         table[y-1][x-1] = 'O'
# #     for y in range(3):
# #         for x in range(3):
# #             if table[y][x] ==
#
#
#
#
#
# # for tc in range(1, int(input())+1):
# #     dec = int(input())
# #     if dec % 2 == 0:
# #         print('even')
# #     else:
# #         print('odd')
#
# # e,f,c = map(int,input().split())
# # tot = (e+f) // c
# # if tot % c ==0:
# #     print(tot + 1)
# # else:
# #     print(tot)
#
# # def fibonacci(n):
# #     a, b = 1, 0
# #     for i in range(n):
# #         a, b = b, a + b
# #     return b
# #
# # print(fibonacci(10))
#
#
# # 0 0 0 0 0
# # 0 0 0 0 0
# # 0 0 0 0 0
# # 0 0 0 0 0
# # 0 0 0 0 0
#
# # P = 5
# # map = [list(map(int, input().split())) for _ in range(P)]
# # for y in range(P):
# #     for x in range(P):
# #         if y == 0:
# #             map[y][x] = 1
# #         print(map[y][x], end=' ')
# #     print()
# # print()
# #
# # for y in range(P):
# #     for x in range(P):
# #         if x == 0:
# #             map[y][x] = 1
# #         print(map[y][x], end=' ')
# #     print()
# # print()
# #
# # for y in range(P):
# #     for x in range(P):
# #         if y == P-1:
# #             map[y][x] = 1
# #         print(map[y][x], end=' ')
# #     print()
# # print()
# #
# # for y in range(P):
# #     for x in range(P):
# #         if x == P-1:
# #             map[y][x] = 1
# #         print(map[y][x], end=' ')
# #     print()
# # print()
# #
# # for y in range(P):
# #     for x in range(P):
# #         if y == x:
# #             map[y][x] = 1
# #         print(map[y][x], end=' ')
# #     print()
# # print()
# #
# # for y in range(P):
# #     for x in range(P):
# #         if y + x == 4:
# #             map[y][x] = 1
# #         print(map[y][x], end=' ')
# #     print()
# # print()
# #
# # L_sums = 0
# # R_sums = 0
# # for y in range(P):
# #     for x in range(P):
# #         if y == x:
# #             L_sums += map[y][x]
# #         if y + x == 4:
# #             R_sums += map[y][x]
# #
# # if L_sums < R_sums:
# #     print(L_sums)
# # else:
# #     print(R_sums)
#
# # 0 0 0 0
# # 0 0 0 0
# # 0 1 0 0
# # 0 0 0 0
#
# maps = [list(map(int, input().split())) for _ in range(4)]
#
# for y in range(4):
#     for x in range(4):
#         if maps[y][x] == 1:
#             print(y,x)
#
# for y in range(4):
#     for x in range(4):
#         if y == x:
#             maps[y][x] = x + 1
#         print(maps[y][x], end=' ')
#     print()
# print()
#
# tmps = 0
# for y in range(4):
#     for x in range(4):
#         if y == x:
#             tmps += maps[y][x]
# print(tmps)
#
# for y in range(1,4):
#     for x in range(1,4):
#         a = 0
#         for yy in range(y):
#             for xx in range(x):
#                 a += maps[yy][xx]
#
#         b = 0
#         for yy in range(y,4):
#             for xx in range(x):
#                 b += maps[yy][xx]
#
#         c = 0
#         for yy in range(y):
#             for xx in range(x, 4):
#                 c += maps[yy][xx]
#
#         d = 0
#         for yy in range(y, 4):
#             for xx in range(x, 4):
#                 d += maps[yy][xx]
#
# print(a+b+c+d)
#
# if a == b == c == d:
#     print(1)
# else:
#     print(2)
#
# for y in range(4):
#     for x in range(4):
#         if y == 0:
#             maps[y][x] = 1
#         print(maps[y][x], end=' ')
#     print()
# print()
#
# for y in range(4):
#     for x in range(4):
#         if x == 0:
#             maps[y][x] = 1
#         print(maps[y][x], end=' ')
#     print()
# print()
#
# for y in range(4):
#     for x in range(4):
#         if y == 4-1:
#             maps[y][x] = 1
#         print(maps[y][x], end=' ')
#     print()
# print()
#
# for y in range(4):
#     for x in range(4):
#         if x == 4-1:
#             maps[y][x] = 1
#         print(maps[y][x], end=' ')
#     print()
# print()
#
# for y in range(4):
#     for x in range(4):
#         if y == x:
#             maps[y][x] = 1
#         print(maps[y][x], end=' ')
#     print()
# print()
#
# for y in range(4):
#     for x in range(4):
#         if y + x == 3:
#             maps[y][x] = 1
#         print(maps[y][x], end=' ')
#     print()
# print()
#
# L_sums = 0
# R_sums = 0
# for y in range(4):
#     for x in range(4):
#         if y == x:
#             L_sums += maps[y][x]
#         if y + x == 3:
#             R_sums += maps[y][x]
#
# if L_sums < R_sums:
#     print(L_sums)
# else:
#     print(R_sums)

# def fibs(n):
#     a,b = 1,0
#     for _ in range(n):
#         a,b = b, b+a
#     return b
# print(fibs(10))
#
#

# import sys
# sys.stdin=open('IM.txt')
# A = list(int(input())for _ in range(7))
# B = [x for x in A if x % 2 != 0]
# if sum(B) > 0:
#     print(sum(B))
#     print(min(B))
# else:
#     print(-1)
#
# N = int(input())
# S = [int(input())for _ in range(N)]
# cnt_i = 0
# cnt_o = 0
# A = 'Junhee is cute!'
# B = 'Junhee is not cute!'
#
# for y in S:
#     if y == 1:
#         cnt_i += 1
#     else:
#         cnt_o += 1
#
# if cnt_i > cnt_o:
#     print(A)
# else:
#     print(B)

# def rots(d,m):
#     N = len(m)
#     ro = [[0] * N for _ in range(N)]
#
#     if d % 4 == 1:
#         for r in range(N):
#             for c in range(N):
#                 ro[c][N-1-r] = m[r][c]
#
#     elif d % 4 == 2:
#         for r in range(N):
#             for c in range(N):
#                 ro[N-1-c][N-1-r] = m[r][c]
#
#     elif d % 4 == 3:
#         for r in range(N):
#             for c in range(N):
#                 ro[N-1-c][r] = m[r][c]
#
#     else:
#         for r in range(N):
#             for c in range(N):
#                 ro[r][c] = m[r][c]
#
#     return ro
#
# test = [[1,2,3],[4,5,6],[7,8,9]]
#
# print(rots(0,test))
# print(rots(1,test))
# print(rots(2,test))
# print(rots(3,test))
# print(rots(4,test))

# 문자열 선택 지우기
# wording = input()
# detection = 'CAMBRIDGE'
# news = []
# for i in wording:
#     if i in detection:
#         pass
#     else:
#         news.append(i)
# print("".join(news))

# for tc in range(1, int(input())+1):
#     wording = input()
#     new_wording = []
#     if len(wording) <= 1:
#         for i in wording:
#             new_wording.append(i)
#         print(new_wording2)
#
#     else:
#         for i in wording:
#             new_wording.append(wording[0])
#             new_wording.append(wording[-1])
#
#         print("".join(new_wording))
# S = []
# for tc in range(1,10):
#     S.append(int(input()))
#     t = max(S)
# print(t)
# print(S.index(t)+1)

# top = []
#
# for t in range(int(input())):
#     quiz = input()
#     sco = 0
#     accu_sco = 0
#     for x in quiz:
#         if x == 'O':
#             sco += 1
#         else:
#             sco = 0
#         accu_sco += sco
#     top.append(accu_sco)
#
# print(*top)

# A = 427
# B = 266
# C = 150
# D = A*B*C
# d_list = list(str(D))
# for i in range(10):
#     d_count = d_list.count(str(i))
#     print(d_count)

# def solves(nums):
#     res = 0
#     for num in nums:
#         res += num
#     return res
#
# nums = [1,2,3,2,1,3,2]
# print(solves(nums))

# for tc in range(1,int(input())+1):
#     N = int(input())
#     FIELD = [input()for _ in range(N)]
#     s = sum([int(i) for i in FIELD[N//2]]) #농작물 수확할 중앙값 구하기
#     # print(s)
#     N //= 2
#     for i in range(N): #필드 기준 분할
#         s += int(FIELD[i][N])
#         s += int(FIELD[-i-1][N])
#         for j in range(i): #필드 row 별 검색
#             s += int(FIELD[i][N+j+1])
#             # print(s)
#             s += int(FIELD[i][N-j-1])
#             # print(s)
#             s += int(FIELD[-i-1][N+j+1])
#             # print(s)
#             s += int(FIELD[-i-1][N-j-1])
#             # print(s)
#     print('#{} {}'.format(tc, s))
#
#
#
# N = 7
# b = 3
# arr = [[0] * N for _ in range(N)]
# max_bomb = 0
#
# for i in range(N):
#     for j in range(N):
#         dia = 0
#         gs = 0
#         for k in range(1, b+1):
#             # 수평, 수직
#             Ax = i;By = j
#             Ay1 = j + k;Ay2 = j - k
#             Bx1 = i + k;Bx2 = i - k
#             if Ay1 < N:
#                 gs += arr[Ax][Ay1]
#             if Ay2 >= 0:
#                 gs += arr[Ax][Ay2]
#             if Bx1 < N:
#                 gs += arr[Bx1][By]
#             if Bx2 >= 0:
#                 gs += arr[Bx2][By]
#
#             # 대각선
#             if Bx2 >= 0 and Ay1 < N:
#                 dia += arr[Bx2][Ay1]
#             if Bx1 < N and Ay2 >= 0:
#                 dia += arr[Bx1][Ay2]
#             if Ay2 >= 0 and Bx2 >= 0:
#                 dia += arr[Bx2][Ay2]
#             if Bx1 < N and Ay1 < N:
#                 dia += arr[Bx1][Ay1]
#
#         max_bomb = max(max_bomb, dia, gs)
#
# print(max_bomb)

# for tc in range(1, int(input())+1):
#     n = int(input())
#     matrix = [[0] * n for _ in range(n)]
#     cnt = 0
#     offset = 0
#     row = n
#     col = n
#
#     while row > 0 and col > 0:
#         for i in range(offset, offset+col):
#             cnt += 1
#             matrix[offset][i] = cnt
#
#         for i in range(offset+1, offset+row):
#             cnt += 1
#             matrix[i][offset+col-1] = cnt
#
#         for i in range(offset+col-2, offset-1, -1):
#             cnt += 1
#             matrix[offset+row-1][i] = cnt
#
#         for i in range(offset+row-2, offset, -1):
#             cnt += 1
#             matrix[i][offset] = cnt
#
#         offset += 1
#         row -= 2
#         col -= 2
#
#     print('#{}'.format(tc))
#     for i in range(0, n):
#         for j in range(0, n):
#             print(matrix[i][j], end=' ')
#         print()


# for tc in range(1, int(input())+1):
#     n = int(input())
#     matrix = [[0] * n for _ in range(n)]
#     direction = 0
#
#     cnt = 1
#     row = 0
#     col = 0
#
#     while cnt <= n * n:
#         matrix[row][col] = cnt
#
#         if direction == 0:
#             if col + 2 > n or matrix[row+0][col+1] != 0:
#                 direction += 1
#
#         elif direction == 1:
#             if row + 2 > n or matrix[row + 1][col + 0] != 0:
#                 direction += 1
#
#         elif direction == 2:
#             if col <= 0 or matrix[row+0][col-1] != 0:
#                 direction += 1
#
#         else:
#             if row <= 0 or matrix[row-1][col+0] != 0:
#                 direction = 0
#
#
#         if direction == 0:
#             col += 1
#         elif direction == 1:
#             row += 1
#         elif direction == 2:
#             col -= 1
#         else:
#             row -= 1
#
#
#         cnt += 1
#
#     print('#{}'.format(tc))
#     for i in range(0, n):
#         for j in range(0, n):
#             print(matrix[i][j], end=' ')
#         print()
#     print(row)
#     print(col)


# for tc in range(1,int(input())+1):
#     box_1 = list(map(int, input().split()))
#     box_2 = list(map(int, input().split()))
#     # print(box_1, box_2)
#     N = 10
#     map = [[0] * N for _ in range(N)]
#     # print(map)
#     x_1 = box_1[0]
#     y_1 = box_1[1]
#     x_2 = box_1[2]
#     y_2 = box_1[3]
#     colors = box_1[4]
#     x__1 = box_2[0]
#     y__1 = box_2[1]
#     x__2 = box_2[2]
#     y__2 = box_2[3]
#     colors_2 = box_2[4]
#     cnt = 0
#     for y in range(y_1, y_2+1):
#         for x in range(x_1, x_2+1):
#             map[y][x] = colors
#
#     for y in range(y__1, y__2+1):
#         for x in range(x__1, x__2+1):
#             if map[y][x] == colors:
#                 map[y][x] = 3
#             else:
#                 map[y][x] = colors_2
#
#     for y in range(N):
#         for x in range(N):
#             if map[y][x] == 3:
#                 cnt += 1
#
#     print('#{} {}'.format(tc, cnt))

# for tc in range(1, 11):
#     field = [list(map(int, input().split())) for _ in range(100)]
#     d_l = 0;
#     d_r = 0
#     max_sum = 0
#
#     for y in range(100):
#         r = 0
#         for x in range(100):
#             r += field[y][x]
#             if max_sum < r:
#                 max_sum = r
#
#     for y in range(100):
#         c = 0
#         for x in range(100):
#             c += field[x][y]
#             if max_sum < c:
#                 max_sum = c
#
#     for y in range(100):
#         d_l += field[y][y]
#         d_r += field[y][99 - y]
#         if max_sum < d_l:
#             max_sum = d_l
#
#         if max_sum < d_r:
#             max_sum = d_r
#
#     print('#{} {}'.format(tc, max_sum))
#
# for tc in range(1, int(input())+1):
#    N = int(input())  #박스 갯수 정해주는 정수
#    cnt = 0 #겹치는 부분을 체크하는 반복수
#    sol=[['0']*10 for _ in range(10)] #게임판, str 으로 넣어 추후에 추출하기 편함
#    data= [[0]*5for _ in range(N)] #박스 좌표와 색상 /// 정수로 받음
#    for i in range(N):
#        data[i] = list(map(int,input().split()))
#    for i in range(N):
#        for j in range(data[i][0],data[i][2]+1):
#            for k in range(data[i][1],data[i][3]+1):
#                sol[j][k] +=str(data[i][4])
#    for i in range(10):
#        for j in range(10):  # 전체 배열을 돌면서 중복되는 부분을 체크 후 cnt 에 추가
#            if '1' in sol[i][j] and '2' in sol[i][j]:
#                cnt+=1
#    print("#{} {}".format(tc,cnt))
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     B = int(input())
#     map = [list(map(int,input().split())) for _ in range(N)]
#     field = [[0]*(N*3) for _ in range(N*3)]
#     res = 0
#     for i in range(N):
#         for j in range(N):
#             field[i+N][j+N] = map[i][j]
#
#     for i in range(n, n*2):
#         for j in range(n, n*2):
#             sums = 0
#             for k in range(1, B+1):
#                 sums += map[i][j+k] #우측합
#                 sums += map[i][j-k] #좌측합
#                 sums += map[i-k][j] #상합
#                 sums += map[i+k][j] #하합
#                 sums += map[i + k][j + k] #우하대각합
#                 sums += map[i - k][j - k] #좌상대각합
#                 sums += map[i + k][j - k] #좌하대각합
#                 sums += map[i - k][j + k] #우상대각합
#
#             if res < sums:
#                 res = sums
#
#     print('#{} {}'.format(tc, res))

# for tc in range(1,int(input())+1):
#     N = int(input())
#     cnt = 0
#     map = [['0'] * 10 for _ in range(10)]
#     data = [[0] * N for _ in range(N)]
#     for i in range(N):
#         data[i] = list(map(int,input().split()))
#     for i in range(N):
#         for j in range(data[i][0], data[i][2]+1):
#             for k in range(data[i][1], data[i][3]+1):
#                 map[j][k] += str(data[i][4])
#
#     for i in range(10):
#         for j in range(10):
#             if '1' in map[i][j] and '2' in map[i][j]:
#                 cnt += 1
#
#     print('#{} {}'.format(tc, cnt))


# for tc in range(1, int(input())+1):
#    N = int(input())
#    cnt = 0
#    sol=[['0']*10 for _ in range(10)]
#    data= [[0]*5for _ in range(N)]
#    print(data)
#    for i in range(N):
#        data[i] = list(map(int, input().split()))
#        print(data)
#    for i in range(N):
#        for j in range(data[i][0],data[i][2]+1):
#            for k in range(data[i][1],data[i][3]+1):
#                sol[j][k] +=str(data[i][4])
#    for i in range(10):
#        for j in range(10):
#            if '1' in sol[i][j] and '2' in sol[i][j]:
#                cnt+=1
#    print("#{} {}".format(tc,cnt))

# for t in range(1,int(input())):
#    n = int(input())
#    array = [[0] * 10 for _ in range(10)]
#
#    for _ in range(n):
#        r1, c1, r2, c2, color = map(int, input().split())
#
#        for i in range(r1, r2 + 1):
#            for j in range(c1, c2 + 1):
#                array[i][j] += color
#
#    purple = 0
#    for row in array:
#        purple += row.count(3)
#
#    print('#{} {}'.format(t, purple))

# for tc in range(1, int(input())+1):
#     N,M = map(int, input().split())
#     rab = [list(map(int,input().split())) for _ in range(M)]
#     farm = [[0] * N for _ in range(N)]
#     m_cat = 0
#     cnt = 0
#     for a in range(M):
#         y = rab[a][0]
#         x = rab[a][1]
#         di = rab[a][2]
#         dt = rab[a][3]
#
#         while (0 <= x < N) and (0 <= y < N):
#             farm[y][x] += 1
#             if m_cat < farm[y][x]:
#                 m_cat = farm[y][x]
#             if di == 0:
#                 y -= dt
#             elif di == 1:
#                 y += dt
#             elif di == 2:
#                 x -= dt
#             else:
#                 x += dt
#
#     for i in range(N):
#         for j in range(N):
#             if farm[i][j] == m_cat:
#                 cnt += 1
#
#     print('#{} {}'.format(tc, cnt))

# cnt = 0
# A = [[0,3,1,3,2,1,4],[4,4,2,3,2,1],[5,5,5,5,5],[1,2,3,4,5,6,7,8,9]]
# for x in A:
#     cnt += x.count(3)
# print(cnt)

# for tc in range(1, int(input())+1):
#     K = int(input())
#     A = [int(input()) for _ in range(K)]
#     for y in range(K):
#         for x in A:
#             if x == 0:
#                 A.pop(A[x-1])
#     B = sum(A)
#
#     print('#{} {}'.format(tc, B))
# res = 0
# A = list(map(int, input().split()))
# for i in str(A):
#     res += int(i)
# print(res)
#
# mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
# print(mylist)
# n_list = list(map(list, zip(*mylist)))
# print(n_list)

for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    card = [y for y in range(1, X + 1)]
    regulation = 2
    check = 0
    ans = 0
    while check == 0:
        for i in range(len(card) - regulation):
            tmp = 0
            for j in range(regulation):
                tmp += card[i + j]

            if i == 0:
                if tmp >= X:
                    check = 1

            if tmp == X:
                leng = regulation
                if ans < leng:
                    ans = leng

                rg += 1

    print('#{} {}'.format(tc, ans))