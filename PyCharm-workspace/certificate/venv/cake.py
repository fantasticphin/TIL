

cake = [[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]

[print(cake[i]) for i in range(4)]
N = 4
result = 2
for y in range(1,N):
    for x in range(1, N):
        # 1면
        a = 0
        for yy in range(y):
            for xx in range(x):
                a += cake[yy][xx]
        # 2면
        b = 0
        for yy in range(y, N):
            for xx in range(x):
                b += cake[yy][xx]

        # 3면
        c = 0
        for yy in range(y):
            for xx in range(x, N):
                c += cake[yy][xx]

        d = 0
        # 4면
        for yy in range(y, N):
            for xx in range(x, N):
                d += cake[yy][xx]




        if a == b == c == d:
            result =1
    print(a, b, c, d)
print(result)