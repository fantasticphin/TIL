#1. 파일 쓰기 (old.v)

# f = open('ssafy.txt', 'w')
# for i in range(10):
#     f.write(f'This is line {i}.\n')
# f.close()

#2. 파일 쓰기 (New.V)

with open('with_ssafy.txt','w') as f:
    for i in range(30):
        f.write(f.'This is line {i}.\n')
