# 20251124 20251125 20251126

# [코드 처리하기]

def solution(code):
    ret = ""                 # 결과 문자열(ret)을 빈 문자열로 초기화
    mode = 0                 # 초기 mode = 0

    for idx in range(len(code)):        # 0 ~ len(code)-1 까지 반복
        if code[idx] == "1":            # '1'이면
            mode = 1 - mode             # mode 토글(0↔1)

        else:                           # '1'이 아닌 문자일 때
            if mode == 0 and idx % 2 == 0:   # mode 0 + 짝수 인덱스
                ret += code[idx]             # ret에 추가
            elif mode == 1 and idx % 2 == 1: # mode 1 + 홀수 인덱스
                ret += code[idx]

    if ret == "":                    # ret 비었으면
        return "EMPTY"
    else:
        return ret                   # 아니면 ret 반환   



# [등차수열의 특정한 항만 더하기]

def solution(a, d, included):
    answer = 0

    for i in range(len(included)):          # included의 인덱스 0~끝까지 반복
        if included[i] == True:             # i번째 항을 선택해야 하면
            answer += a + d * i             # 등차수열의 i번째 항 값을 더함

    return answer                           # 최종 합계 반환



# [주사위 게임 2]

def solution(a, b, c):
    s1 = a + b + c
    s2 = a*a + b*b + c*c
    s3 = a*a*a + b*b*b + c*c*c

    if a == b == c:               # 세 개 모두 같음
        return s1 * s2 * s3

    if a == b or a == c or b == c:  # 두 개만 같음
        return s1 * s2

    return s1                     # 모두 다름



# [원소들의 곱과 합]

# 첫 번째 방법

def solution(num_list):
    mul = 1        # 곱을 저장할 변수(초기값 1)

    for n in num_list:
        mul *= n   # 리스트 안의 숫자들을 모두 곱함
    
    sum_value = sum(num_list)   # 리스트의 모든 숫자를 더한 값

    if mul < sum_value**2:      # 곱이 (합의 제곱)보다 작은지 비교
        return 1                # 작으면 1 반환
    else:
        return 0                # 아니면 0 반환

# 두 번째 방법
  
def solution(num_list):
    mul = 1                       # 모든 원소의 곱을 저장할 변수(곱은 1부터 시작!)
    
    for n in num_list:
        mul *= n                  # 리스트의 숫자들을 하나씩 모두 곱함
    
    # mul이 (리스트 합의 제곱)보다 작으면 True(1), 아니면 False(0)
    return int(mul < sum(num_list) ** 2)



# [이어 붙인 수]

def solution(num_list):
    odd_str = ""   # 홀수만 이어 붙일 문자열
    even_str = ""  # 짝수만 이어 붙일 문자열

    for n in num_list:
        if n % 2 == 1:       # n이 홀수라면
            odd_str += str(n)   # 문자열로 바꿔 이어 붙인다
        else:                # n이 짝수라면
            even_str += str(n)  # 문자열로 바꿔 이어 붙인다

    # 문자열을 정수로 변환해서 더해 결과 반환
    return int(odd_str) + int(even_str)



# [수열과 구간 쿼리 3]

def solution(arr, queries):
    # queries의 모든 쌍(i, j)에 대해 arr[i]와 arr[j]를 교환한다
    for i, j in queries:
        # 두 위치의 값을 서로 바꾸기 (swap)
        arr[i], arr[j] = arr[j], arr[i]

    return arr



# [수열과 구간 쿼리 2]

def solution(arr, queries):
    answer = []  # 각 쿼리의 결과를 저장할 리스트

    for s, e, k in queries:                # 쿼리 하나([s, e, k])씩 꺼내기
        min_value = float('inf')          # 처음에는 '무한대'로 둔다 (아직 찾은 값 없음 표시)

        # s부터 e까지(포함) 인덱스를 하나씩 검사
        for i in range(s, e + 1):
            # arr[i]가 k보다 크다면 후보가 된다
            if arr[i] > k:
                # 후보 중 가장 작은 값으로 갱신
                # min_value가 무한대였으면 arr[i]로 바뀌고,
                # 아니라면 기존 min_value와 arr[i] 중 더 작은 값을 선택
                min_value = min(min_value, arr[i])

        # 만약 min_value가 아직 float('inf')라면:
        # -> for문 동안 k보다 큰 값을 한 번도 만나지 못했다는 뜻
        # -> 조건을 만족하는 값이 없으므로 -1을 정답에 추가
        if min_value == float('inf'):
            answer.append(-1)
        else:
            # 그렇지 않으면(한 번 이상 갱신되어 실제 값이 들어있으면)
            # 그 값을 결과로 추가
            answer.append(min_value)

    return answer

# 예시 - 최솟값 찾기

# float('inf') 사용 예
min_value = float('inf')
for x in [10, 5, 20]:
    if x < min_value:
        min_value = x
print(min_value)  # 5
