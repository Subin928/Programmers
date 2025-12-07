# 20251207

# [배열 만들기 5]

# 문제 이해
# 1. 각 문자열에서 인덱스 s부터 길이 l만큼 추출
# 2. 추출한 부분을 정수로 변환
# 3. k보다 큰 값만 배열에 담아 반환


# 방법 1. 리스트 컴프리헨션 
def solution(intStrs, k, s, l):
    return [int(string[s:s+l]) for string in intStrs if int(string[s:s+l]) > k]


# 방법 2. for 루프
def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        # s부터 l까지 문자 추출
        substring = string[s:s+l]
        # 정수로 변환
        num = int(substring)
        # k보다 크면 추가
        if num > k:
            result.append(num)

    return result


# 방법 3. 중복 계산 방지

def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        num = int(string[s:s+l])
        if num > k:
            result.append(num)
    return result


# 핵심 포인트
# 1. 슬라이싱: string[s:s+l] -> s부터 l개 문자 추출
# 2. 형변환: int(substring) -> 문자열을 정수로
# 3. 조건 필터링 if num > k


# 예시

s = '0123456789'
# 인덱스: 0123456789

# s=5, l=5
substring = s[5:5+5]
# 인덱스 5부터 9까지 (10 미포함)
# 56789

# 시작(5) 포함, 끝(10) 미포함



# [부분 문자열 이어 붙여 문자열 만들기]

# 문제 이해
# 각 문자열에서 지정된 구간만 추출해서 순서대로 이어붙이기


# 방법 1. 리스트 컴프리헨션 + join

def solution(my_strings, parts):
    return ''.join([my_strings[i][s:e+1] for i, (s, e) in enumerate(parts)])


# 방법 2. for 루프

def solution(my_strings, parts):
    result = ''
    for i in range(len(parts)):
        s, e = parts[i]
        result += my_strings[i][s:e+1]

    return result


# 방법 3. zip 사용

def solution(my_strings, parts):
    return ''.join([string[s:e+1] for string, (s,e) in zip(my_strings, parts)])


# 코드 설명

def solution(my_strings, parts):
    result = []

    # enumerate로 인덱스와 값을 동시에 가져오기
    for i, (s, e) in enumerate(parts):
        # i = 0, 1, 2, 3, ...
        # s, e : parts[i]의 시작과 끝 인덱스

        # my_strings[i]에서 s부터 e까지 추출
        substring = my_strings[i][s:e+1]
        result.append(substring)

    # 모든 부분 문자열을 이어붙이기
    return ''.join(result)

# 핵심 포인트

# 1. enumerate로 인덱스와 값을 동시에 가져오기
# 2. 언패킹 : (s, e) = parts[i]
# 3. 슬라이싱: string[s:e+1] (e 포함!)
# 4. join: 여러 문자열을 하나로 합치기


# enumerate vs zip vs range

my_strings = ["abc", "def"]
parts = [[0, 1], [1, 2]]

# enumerate 방법 (인덱스 필요할 때)

for i, (s, e) in enumerate(parts):
    print(i, s, e, my_strings[i][s:e+1])
# 0 0 1 ab
# 1 1 2 ef


# zip 방법 (동시 순회)

for string, (s, e) in zip(my_strings, parts):
    print(string, s, e, string[s:e+1])
# abc 0 1 ab
# def 1 2 ef


# range 방법 (명시적 인덱스)

for i in range(len(parts)):
    s, e = parts[i]
    print(i, s, e, my_strings[i][s:e+1])
# 0 0 1 ab
# 1 1 2 ef