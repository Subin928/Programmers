# 20251203

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