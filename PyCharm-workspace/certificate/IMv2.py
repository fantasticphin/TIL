import sys
sys.stdin = open('IM.txt')


for tc in range(1, int(input()) + 1):
    B = int(input())
    table = [list(map(int, input().split())) for _ in range(B)]
    winner = 0
    dd = 0
    result = 2
    for i in range(B):
        for j in range(B):
            if table[i][j] == 1:
                # x축 탐색
                dd = 0
                for x in range(j, B):
                    if table[i][x] == 1:
                        dd += 1
                    else:
                        break
                if dd == 5:
                    result = 1


                # y축탐색
                dd = 0
                for y in range(i, B):
                    if table[y][j] == 1:
                        dd += 1
                    else:
                        break
                if dd == 5:
                    result = 1


                # \대각선
                dd = 0
                for k in range(5):
                    if i+k < B and j+k < B:
                        if table[i+k][j+k] == 1:
                            dd += 1
                        else:
                            break
                if dd == 5:
                    result = 1

                # /대각선
                dd = 0
                for k in range(5):
                    if i + k < B and j - k >= 0:
                        if table[i + k][j - k] == 1:
                            dd += 1
                        else:
                            break
                if dd == 5:
                    result = 1

    print('#{} {}'.format(tc, result))



            # for x in range(B):
            #     for y in range(B):
            #         for table[x][y] in table:
            #             if table[x][y] == table[x][y+1]:
            #                 winner = 1
            #             else:
            #                 winner = 2
            # for a in range(B):
            #     for b in range(B):
            #         for table[b][a] in table:
            #             if table[b][a] == table[b][a+1]:
            #                 winner = 1
            #             else:
            #                 winner = 2

    print('{} {}'.format(tc, result))





