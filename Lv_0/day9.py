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


# [문자열의 뒤의 n 글자]

# 문제 이해
# 문자열의 뒤에서 n개 글자 추출


# 방법 1. 음수 인덱스 슬라이싱

def solution(my_string, n):
    # 음수 인덱스로 뒤에서부터 n개 추출
    return my_string[-n:]


# 방법 2. 길이 계산

def solution(my_string, n):
    return my_string[len(my_string)-n:]


# 음수 인덱스 이해하기

s = "abcde"
# 양수 인덱스 : 0 1 2 3 4 5
# 음수 인덱스 : -5 -4 -3 -2 -1

# 뒤에서 3개
s[-3:] # cde

# 뒤에서 1개
s[-1:] # d

# 뒤에서 5개 (전체)
s[-5:] # abcde


# 주의사항

# n이 문자열 길이보다 클 때
s = "abc"
n = 10

print(s[-10:]) # "abc"

# Python은 슬라이싱 범위 초과 시 자동으로 조정됨


# 핵심 포인트
# 1. 음수 인덱스: 뒤에서부터 세기
#  -1: 마지막
#  -2: 마지막에서 두 번째
#  -n : 마지막에서 n번째

# 2. 슬라이싱: [시작:]
#  끝 생략하면 끝까지

# 3. 간결함: [-n:]이 최선!



# [접미사 배열]

# 문제 이해
# 접미사(suffix) : 특정 인덱스부터 끝까지의 문자열
# "banana"의 접미사: "banana", "anana", "nana", "ana", "na", "a"


# 방법 1. 리스트 컴프리헨션 + sorted
def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])


# 방법 2. for 루프
def solution(my_string):
    suffixes = []
    for i in range(len(my_string)):
        suffixes.append(my_string[i:])
    return sorted(suffixes)


# 방법 3. sort() 사용
def solution(my_string):
    # 1단계: 모든 접미사 생성
    suffixes = [my_string[i:] for i in range(len(my_string))]
    # 2단계: 사전순 정렬
    return sorted(suffixes)


# 핵심 포인트
# 1. 접미사 생성: my_string[i:] (i부터 끝까지)
# 2. range: range(len(my_string))으로 모든 인덱스
# 3. 정렬: sorted()함수로 사전순 정렬

# sorted vs sort

suffixes = ["banana", "anana", "nana"]

# sorted(): 새 리스트 반환 (원본 유지)
result = sorted(suffixes)
print(suffixes) # ["banana", "anana", "nana"] (원본 그대로)
print(result) # ["anana", "banana", "nana"] (정렬된 새 리스트)

# sort(): 원본 수정 (반환값 None)
suffixes.sort()
print(suffixes) # ["anana", "banana", "nana"] (원본 변경됨)



# [접미사인지 확인하기]

# 문제 이해
# 주어진 문자열이 접미사인지 확인
#  - 접미사면 1 반환
#  - 아니면 0 반환


# 방법 1. endswith() 사용
def solution(my_string, is_suffix):
    # endwith(): 문자열이 특정 접미사로 끝나는지 확인
    return 1 if my_string.endswith(is_suffix) else 0

# 예:
# "banana".endswith("ana") -> True
# "banana".endswith("nan") -> False

# 방법 2. 슬라이싱 비교
def solution(my_string, is_suffix):
    # 뒤에서 is_suffix 길이만큼 추출해서 비교
    return 1 if my_string[-len(is_suffix):] == is_suffix else 0

# 예:
# "banana"[-3:] = "ana" 
# "ana" == "ana" -> True -> 1

# 방법 3. 접미사 리스트 생성
def solution(my_string, is_suffix):
    suffixes = [my_string[i:] for i in range(len(my_string))]
    return 1 if is_suffix in suffixes else 0


# 핵심 포인트
# 1. endswith(): 문자열이 특정 접미사로 끝나는지 확인하는 내장 메서드
# 2. 슬라이싱: [-n:]으로 뒤에서 n글자 추출
# 3. 조건문: Ture면 1, False면 0 반환

# 예제 1: 전체 문자열
print(solution("hello", "hello"))  # 1

# 예제 2: 마지막 1글자
print(solution("world", "d"))      # 1

# 예제 3: 접미사 아님
print(solution("python", "py"))    # 0 (접두사임!)

# 예제 4: 빈 문자열
print(solution("test", ""))        # 1 (빈 문자열은 모든 문자열의 접미사)

# 예제 5: 더 긴 문자열
print(solution("hi", "hello"))     # 0 (원본보다 김)