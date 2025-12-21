# 20251221

# [리스트 자르기]

# 설명
# 정수 n (1~4)
# slicer 리스트에 3개의 정수 [a, b, c]
# num_list를 n의 값에 따라 다르게 슬라이싱


# 풀이

def solution(n, slicer, num_list):
    a, b, c = slicer

    if n == 1:
        # 0번 인덱스부터 b번 인덱스까지
        return num_list[:b+1]
    elif n == 2:
        # a번 인덱스부터 마지막 인덱스까지
        return num_list[a:]
    elif n == 3:
        # a번 인덱스부터 b번 인덱스까지
        return num_list[a:b+1]
    else: # n ==4
        # a번 인덱스부터 b번 인덱스까지 c 간격으로
        return num_list[a:b+1:c]



# [첫 번째로 나오는 음수 찾기]

# 설명
# 리스트를 순회하면서 첫 번째 음수를 찾으면 그 인덱스 반환
# 없으면 -1 반환

# 풀이
# - enumerate(num_list): 인덱스와 값을 함께 반환 (0, 12), (1, 4), ...


# 방법 1
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1


# 방법 2. enumerate 사용
def solution(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i
    return -1



# [배열 만들기]

# 설명
# 두 개의 구간을 배열에서 추출해서 합치는 문제
# 닫힌 구간이므로 양 끝 포함
# arr[a:b+1]


def solution(arr, intervals):
    answer = []
    for a,b in intervals: answer+=arr[a:b+1]
    return answer



# [2의 영역]

# 설명
# 2가 처음 나타나는 위치부터 마지막으로 나타나는 위치까지의 부분 배열 반환


# 방법 1
def solution(arr):
    if 2 not in arr:
        return [-1]
    # 첫 번째 2의 인덱스부터 마지막 2의 인덱스(뒤에서부터 찾기)
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]


# 방법 2 - 리스트 컴프리헨션
def solution(arr):
    # 2의 모든 인덱스 찾기
    indices = [i for i, num in enumerate(arr) if num == 2]

    if not indices:
        return [-1]
    # indices[-1]: 마지막 2의 인덱스, arr[first:last+1]: 첫 번째부터 마지막까지 슬라이싱
    return arr[indices[0]:indices[-1] + 1]



# [배열 조각하기]

# 설명

# 1. query를 순회하면서:
#   - query 인덱스가 짝수 -> arr에서 query[i]번 인덱스를 제외하고 그 뒷부분 잘라서 버림
#   - query 인덱스가 홀수 -> arr에서 query[i]번 인덱스를 제외하고 그 앞부분 잘라서 버림

# 예시)
# arr = [0,1,2,3,4,5]
# query = [4,1,2]
# i=0(짝수): query[0]=4 -> arr[4]번 인덱스를 제외하고 뒷부분 제거


# 방법 1.
def sollution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:           # 짝수 인덱스
            # query[i]번 인덱스까지만 남기고 뒷부분 제거
            arr = arr[:query[i]+1]
        else:                    # 홀수 인덱스
            # query[i]번 인덱스부터 남기고 앞부분 제거
            arr = arr[query[i]:]
    return arr


# 방법 2. - enumerate 사용
def solution(arr, query):
    for i, q in enumerate(query):
        if i % 2 == 0: # 짝수 인덱스
            arr = arr[:q+1]
        else:
            arr = arr[q:]
    return arr



# [n개 간격의 원소들]

# 설명
# num_list[start:end:step]
#   - start부터 end-1까지 step간격으로
#   - 처음부터 끝까지 n간격이므로 -> [::n]

def solution(num_list, n):
    return num_list[::n]