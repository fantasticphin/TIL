lunch ={
    '자금성': '02-321-3434',
    '밥풀뗴기': '02-333-5454',
    '콩국': '02-874-6841'
}

#1. 방법 1

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        # print(item)
        # print(type(item))
        f.write(f'{item[0]}, {item[1]}\n')
