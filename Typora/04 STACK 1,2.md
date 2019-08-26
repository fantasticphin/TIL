# 04 STACK 1 ~ 2

## 스택 개념

자료를 쌓아 올린 형태의 자료구조

선형구조(자료 간의 1대1 관계, 1|| 비선형은 1대 N 관계<tree>)

스택에 자료 삽입 및 분출

last in first out 후입 선출 (1,2,3, 넣으면 분출시에는 3,2,1 순으로 적용)

## 스택 구현

자료를 선형으로 저장할 저장소가 필요

마지막 삽입된 원소 위치 => TOP 이라 부름, stack == 저장소

1. 삽입 -> push// 자료 저장
2. 삭제 -> pop 자료 꺼냄, 역순
3. 공백 여부 -> isEmpty 로 공백 여부 확인
4. peek -> 스택의 top에 있는 item을 반환

## 스택 삽/삭 과정

공백 스택 => top= -1 => push A => top=A => push B => top = B => push C => top = C

스택 => pop c => top = B

push 알고리즘 -> def push(item):  -> s.append(item)

pop 알고리즘 -> def pop(): -> if len(s) == 0: #underflow return -> else: return s.pop(-1)

*조심할 부분 -> 항상 POP 을 쓸 때 유의!!!!, empty인 상황일 때 pop을 써버리면 none 이 뜸

```python
def pop():
    if len(s) == 0:
        return
    else:
        return s.pop(-1)
```



## 스택 연산

```python
def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print('stack empty') #underflow
        return
    else:
        return pop(-1)
    
s = []
push(1)
push(2)
push(3)
print('pop item=>',pop())
print('pop item=>',pop())
print('pop item=>',pop())
```

## 스택 고려사항

리스트로 스택 구현시

: **구현이 용이**하지만, 크기를 변경하는 작업은 **내부적으로 큰 overhead 발생** 작업으로 많은 시간이 소요

: 배열처럼 크기를 미리 정해놓고 사용, 동적 연결리스트 이용하여 저장소를 동적으로 할당해 스택을 구현



## 스택응용

### 괄호검사

1. [], {}, ()
2.  **조건 1** :왼쪽과 오른쪽 괄호의 개수가 같아야 함
3. **조건 2** : 같은 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 함
4. **조건 3** : 괄호 사이에는 포함 관계만 존재함

개방 괄호가 push됨

또 개방 괄호가 추가 push 됨

닫는 괄호가 올 시, pop을 통해 비교를 함

패턴이 종료된 후, 스택에 남아있다면 오류!

## Memoization

: 이전 계산값을 메모리에 저장, 매번 다시 계산하지 않도록 해, 전체적 실행속도를 향상시킴

:동적계획법의 핵심이 되는 기술

:memoization

```python
def fibo1(n):
    global memo
    if n > 2 and len(memo) < n:
        memo.append(fibo1(n-1)+fibo1(n-2))
    return memo[n]

memo = [0,1]
```



## DP 동적 계획법

: dynamic programming 약자, 	최적화 문제 해결 알고리즘

- 해결순서
- 1. 입력 크기 작은 부분 문제들을 모두 해결 후, 해들을 이용하여 보다 큰 문제를 해결
  2. 궁극적으로 원래 주어진 입력의 문제를 해결

```python
피보나치 수를 dp에 적용한 알고리즘

def fibo2(n):
    f = [0,1]
   
	for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    
    return f[n]
```

## DFS 깊이 우선 탐색

: 비선형구조인 그래프 구조, 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

1. 깊이우선 탐색(depth first search, dfs)
2. 너비 우선 탐색(breadth first search, bfs)
3. 

시작점에서 출발해 존재하는 경로가 있는 곳까지 깊게 탐색, 길이 없으면 마지막 갈림길 간선에서 다른 방향으로 탐색

갈림길 정점을 되돌아가 반복함으로 스택의 후입선출 사용

```python
DFS_Recursive(G, V)

 visited[V] <- TRUE // V 방문 설정
    for each all w in adjacency(G, V)
    if visited[w] != TRUE
    DFS_Recursive
```

**노드 개수에 비해 엣지 개수가 훨씬 적은 그래프라면 인접 행렬보다는 인접 리스트를 사용하는 게 탐색에 효율적이다. 전체 노드가 아닌 연결된 노드만 살펴보면 되기 때문이다. 또한, 인접 리스트는 엣지 개수에 비례하는 메모리만 차지하는 장점이 있다. 단, 두 노드의 연결관계를 알고싶을 때는 인접 행렬이 효율적이다.





# 2019. 08. 26. Stack 2

문자열 수의 계산의 일반적 방법 

1.중위표기법

: 연산자를 피연산자의 가운데 표기하는 방법  => A + B

2.후위표기법

:연산자를 피연산자 뒤에 표기하는 방법  => AB+

** 중위에서 후위로 변환하는 방법**

A.수식의 각 연산자에 대해 우선순위에 따라 괄호를 사용해 다시 표현

B.각 연산자를 그에 대응하는 우측괄호 뒤에 배치

C.괄호를 제거

ex :> ((A*B) - (C/D)) -> ((A B) * (C D) / ) -   -> AB*CD/-

------------------------------------------------------------------------------

왼쪽 괄호는 무조건 ***'PUSH'***

우선순위가 높으면 push

우선순위가 낮으면 pop

## 후위표기법의 수식을 스택을 이용해 계산

1.피연산자를 만나면 스택에 push

2.연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산, 연산결과를 다시 스택에 push

3.수식이 끝나면, 마지막으로 스택을 pop하여 출력한다



# 백트래킹

## 백트래킹
: 답을 찾는 중, '막히면' 되돌아가서 다시 답을 찾아 가는 기법, ***최적화 & 결정*** 문제를 해결할 수 있다.

: 경로 찾기 시도 횟수를 줄임, 불필요 경로 조기에 차단

## 재귀 호출 통한 순열 생성

```python
// arr[] : 데이터가 저장된 배열
// swap(i, j): arr[i] <--교환--> arr[j]
// n: 원소의 개수, k: 현재까지 교환된 원소의 개수
perm( n, k )
IF k == n
print array // 원하는 작업 수행
ELSE
FOR i in k -> n-1
swap(k, i);
perm(n, k + 1);
swap(k, i);

```



## 분할 정복 알고리즘

: 나폴레옹이 연합군을 각개격파 할 때 사용한 전략, 반으로 나누어 각 연합군을 격파

분할 -> 정복 -> 필요시 통합

```python
def power(be, exp):
    if exp == 0 or be == 0:
        return 1
    if exp % 2 == 0:
        NeBe = power(be, exp/2)
        return NeBe * NeBe
    else:
        NeBe = power(be, (exp-1)/2)s
        return (NeBe * NeBe) * be
```

## 퀵 정렬

주어진 배열을 분할, 기준 아이템 중심으로 작은 것은 왼편, 큰것은 오른편으로 정리

```python
def quicksort(a,begin, end):
    if begin < end:
        p = patition(a,begin,end)
        quicksort(a,begin,p-1)
        quicksort(a,p+1,end)
        
def partition(a,begin,end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(a[L]<a[pivot] and L<R): L+=1
        while(a[R]>a[pivot] and L<R): R-=1
        if L<R:
            if L==pivot : pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
	return R
```

