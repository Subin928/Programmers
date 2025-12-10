# 20251210

# [문자열의 앞의 n글자]

# 풀이
# 1. my_string[:n]: 문자열의 처음부터 n번째 인덱스 직전까지 추출
# 2. 즉, 앞에서부터 n개의 문자를 가져옴

def solution(my_string, n):
    return my_string[:n]

# 참고
# n이 문자열 길이보다 크면 전체 문자열이 반환
# n이 0이면 빈 문자열 ""이 반환



# [접두사인지 확인하기]

# 풀이
# 1. my_string.startswith(is_prefix): my_string이 is_prefix로 시작하면 True, 아니면 False
# 2. 조건식을 사용해 True면 1, False면 0을 반환


# 방법 1(권장)
def solution(my_string, is_prefix):
    return 1 if my_string.startswith(is_prefix) else 0


# 방법 2 - 슬라이싱을 사용한 방법
def solution(my_string, is_prefix):
    return 1 if my_string[:len(is_prefix)] == is_prefix else 0



# [문자열 뒤집기]

# 풀이
# 1. my_string[:s] -> 인덱스 s이전 부분 (그대로 유지)
# 2. my_string[s:e+1][::-1] -> 인덱스 s부터 e까지 부분을 뒤집기
# 3. my_string[e+1:] -> 인덱스 e 이후 부분 (그대로 유지)


# 방법 1(권장)
def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]


# 방법 2(리스트 변환)
# 문자열은 immutable(수정 불가)이므로 리스트처럼 슬라이싱에 대입 안돼서 변환 필요

def solution(my_string, s, e):
    result = list(my_string)
    result[s:e+1] = result[s:e+1][::-1]
    return ''.join(result)



# [세로 읽기]

# 설명
# 문자열을 m개씩 나누어 배치했을 때, c번째 열의 문자들을 추출하는 문제

# 풀이
# c-1 : c번째 열은 인덱스로는 c-1(1번째 열 = 인덱스 0)
# range(c-1, len(my_string), m):
#   - 시작 : c-1 (첫 번째 행의 c번째 열)
#   - 끝 : 문자열 끝까지
#   - 간격 : m (한 줄에 m글자씩이므로)


# 방법 1
def solution(my_string, m, c):
    result = ""
    for i in range(c-1, len(my_string), m):
        result += my_string[i]
    return result


# 방법 2(리스트 컴프리헨션)
def solution(my_string, m, c):
    return ''.join([my_string[i] for i in range(c-1, len(my_string), m)])



# [qr code]

# 설명
# 인덱스를 q로 나눈 나머지가 r인 위치의 문자들을 추출하는 문제

# 풀이
# i % q == r : 인덱스 i를 q로 나눈 나머지가 r인지 확인
# 조건을 만족하는 위치의 문자들을 순서대로 이어붙임


# 방법 1
def solution(q, r, code):
    result = ''
    for i in range(len(code)):
        if i % q == r:
            result += code[i]
    return result


# 방법 2 (슬라이싱)
def solution(q, r, code):
    return code[r::q] # code[r::q] -> 인덱스 r부터 시작해서 q칸씩 건너뛰며 추출


# 방법 3 (리스트 컴프리헨션)
def solution(q, r, code):
    return ''.join([code[i] for i in range(len(code)) if i % q == r])