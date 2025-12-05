# 20251203 20251204

# [수열과 구간 쿼리 4]

# 문제 이해
# 1. arr 배열이 주어짐
# 2. queries = [[s, e, k], [s, e, k],...] 형태
# 3. 각 쿼리마다:
#       * s 이상 e 이하의 인덱스 i 중에서
#       * i 가 k의 배수이면
#       * arr[i]에 1을 더함

def solution(arr, queries):
    for s, e, k in queries:      # queries의 각 [s,e,k] 순회
        for i in range(s, e+1):  # s부터 e까지 (e 포함)
            if i % k == 0:       # i가 k의 배수인지 확인
                arr[i] += 1      # 조건 만족하면 1 증가
    return arr



# [배열 만들기2]

# 문제 이해
# 1. l 이상 r 이하의 정수 중에서
# 2. "0"과 "5"로만 이루어진 숫자 찾기
# 3. 오름차순 배열로 반환
# 4. 없으면 [-1] 반환
# 5. 예시 : 5, 50, 55, 500, 505, 550, 555 등

def solution(l, r):
    result = []

    for num in range(l, r+1):
        str_num = str(num)                          # 숫자를 문자열로 변환

        if all(digit in '05' for digit in str_num): # 0과 5로만 이루어져 있는지 확인
            result.append(num)
    
    return result if result else [-1]               # 결과가 없으면 [-1] 반환


def solution(l, r):
    result = []

    for num in range(l, r+1):
        if set(str(num)) <= {'0', '5'}:  # set(str(num)) <= {'0', '5'}는 숫자의 모든 자릿수가 0과 5로만 이루어져 있는지 확인
            result.append(num)

    return result if result else [-1]

# 예제 실행
print(solution(5, 555))  # [5, 50, 55, 500, 505, 550, 555]
print(solution(10, 20))  # [-1] (0과 5로만 이루어진 숫자 없음)
print(solution(1, 10))   # [5] (5만 해당)



# [카운트 업]

# 문제 이해
# start_num부터 end_num까지의 연속된 정수를 리스트로 반환

# 방법 1. range 사용

def solution(start_num, end_num):
    return list(range(start_num, end_num+1))

# 방법 2. 리스트 컴프리헨션

def solution(start_num, end_num):
    return [i for i in range(start_num, end_num+1)]

# 방법 3. for 루프

def solution(start_num, end_num):
    result = []
    for i in range(start_num, end_num+1):
        result.append(i)
    return result



# [콜라츠 수열 만들기]

# 문제 이해
# 콜라츠 수열 규칙:
# x가 짝수 -> x / 2
# x가 홀수 -> 3 * x + 1
# x가 1이 될 때까지 반복
# 거쳐간 모든 수를 기록

def solution(n):
    result = [n]              # 첫 번째 값부터 기록

    while n != 1:             # 1이 될 때까지 반복
        if n % 2 == 0:        # 짝수인 경우
            n = n // 2        # 2로 나누기
        else:                 # 홀수인 경우
            n = 3 * n + 1     # 3배 + 1

        result.append(n)      # 계산 결과 추가
    
    return result



# [배열 만들기 4]

# 문제 이해
# 규칙:
# 1. stk가 비어있으면 -> arr[i] 추가, i += 1
# 2. stk[-1] < arr[i]이면 -> arr[i] 추가, i += 1
# 3. stk[-1] >= arr[i]이면 -> stk[-1] 제거 (i는 그대로!)
# 핵심: 3번 조건에서 i를 증가시키지 않음

def solution(arr):
    stk = []                                  # 빈 배열로 시작
    i = 0                                     # 인덱스 초기값

    while i < len(arr):                       # arr 끝까지 반복
        # 1. stk가 비어있으면
        if not stk:
            stk.append(arr[i])                # 현재 값 추가
            i += 1                            # 다음으로 이동
        
        # 2. stk의 마지막 원소 < arr[i]
        elif stk[-1] < arr[i]:                # 마지막 값 < 현재 값
            stk.append(arr[i])                # 현재 값 추가
            i += 1                            # 다음으로 이동
        
        # 3. stk의 마지막 원소 >= arr[i]
        else:                                 # 마지막 값 >= 현재 값
            stk.pop()                         # 마지막 값 제거
                                              # i는 그대로! (중요)
    return stk

# (간결한 버전)

def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if stk and stk[-1] >= arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
            i += 1
    return stk