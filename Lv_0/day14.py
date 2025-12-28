# 20251228

# [홀수 vs 짝수]

# 설명
# 홀 수 번째 인덱스: 0, 2, 4, .. / 짝수 번째 인덱스: 1, 3, 5, ...

# 풀이

# 방법 1
def solution(num_list):
    odd_sum = sum(num_list[i] for i in range(0, len(num_list), 2))
    even_sum = sum(num_list[i] for i in range(1, len(num_list), 2))

    return max(odd_sum, even_sum)

# 방법 2
def solution(num_list):
    return max(sum(num_list[::2], sum(num_list[1::2])))



# [5명씩]

# 설명
# 5명씩 그룹을 나누어 각 그룹의 첫 번째 사람을 추출하는 함수
# range(0, len(names), 5)를 사용하여 0,5,10,15,... 인덱스 접근

# 풀이

# 방법 1
def solution(names):
    return [names[i] for i in range(0, len(names), 5)]

# 방법 2
def solution(names):
    return names[::5]



# [할 일 목록]

# 설명
# 완료하지 못한 할 일들을 필터링하는 함수
# zip(): 두 개 이상의 리스트를 짝지어주는 함수
# todo_list = ["problemsolving", "practiceguitar", "swim"]
# finished = [True, False, True]
# zip으로 묶으면
# 결과: [("problemsolving", True), ("practiceguitar", False), ("swim", True)]

# 풀이

# 방법 1
def solution(todo_list, finished):
    return [todo for todo, is_finished in zip(todo_list, finished) if not is_finished]

# 방법 2
def solution(todo_list, finished):
    result = []

    # zip으로 두 리스트를 짝지어서 반복
    for todo, is_finished in zip(todo_list, finished):
        # 완료하지 못한 것만 추가
        if not is_finished:
            result.append(todo)

    return result



# [n보다 커질 때까지 더하기]

# 설명
# 배열의 원소를 더하다가 합이 n을 초과하는 순간의 합을 구하는 함수

# 풀이

def solution(numbers, n):
    total = 0
    for num in numbers:
        total += num
        if total > n:
            break
    return total



# [수열과 구간 쿼리 1]

# 설명
# 주어진 범위의 모든 원소에 1씩 더하는 함수
# queries의 각 쿼리 [s, e]를 하나씩 처리
# for s, e in queries: 각 쿼리에서 시작 인덱스 s와 끝 인덱스 e
# range(s, e+1)
# arr[i] += 1: 해당 인덱스의 값을 1 증가

# 풀이

# 방법1
def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1
    return arr

# 예시
print(solution([0, 1, 2, 3, 4], [[0, 1], [1, 3], [2, 4]]))
# [1, 3, 4, 4, 4]

# 초기: [0, 1, 2, 3, 4]
# 
# 쿼리 1: [0, 1] → 인덱스 0, 1에 +1
# [0+1, 1+1, 2, 3, 4] = [1, 2, 2, 3, 4]
#
# 쿼리 2: [1, 3] → 인덱스 1, 2, 3에 +1
# [1, 2+1, 2+1, 3+1, 4] = [1, 3, 3, 4, 4]
#
# 쿼리 3: [2, 4] → 인덱스 2, 3, 4에 +1
# [1, 3, 3+1, 4+1, 4+1] = [1, 3, 4, 5, 5]


# 단계별 풀어쓰기

def solution(arr, queries):
    # queries의 각 쿼리를 순서대로 처리
    for query in queries:
        s = query[0]
        e = query[1]

        # s부터 e까지 (e포함) 모든 인덱스에 대해
        for i in range(s, e+1):
            arr[i] = arr[i] + 1
    
    return arr

