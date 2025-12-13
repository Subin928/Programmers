# 20251210 20251213

# [가까운 1 찾기]

# 설명
# 각 알파벳의 개수를 세어 배열로 만드는 문제

# 풀이
# 1. result = [0] * 52 -> 길이 52의 배열 생성 (A-Z 26개 + a-z 26개)
# 2. ord(char) -> 문자를 아스키 코드 숫자로 변환
# 3. 대문자 (A-Z):
#   - ord(char) - ord('A'): A=0, B=1, C=2, ..., Z=25
#   - 인덱스 0~25에 저장
# 4. 소문자 (a-z):
#   - ord(char) - ord('a') + 26: a=26, b=27,..., z=51
#   - 인덱스 26~51에 저장


# 방법 1
def solution(my_string):
    result = [0] * 52

    for char in my_string:
        if "A" <= char <= "Z":
            result[ord(char) - ord("A")] += 1
        elif "a" <= char <= "z":
            result[ord(char) - ord("a") + 26] += 1
    
    return result


# 방법 2 (count 사용)
def solution(my_string):
    result = []

    # A-Z
    for i in range(26):
        result.append(my_string.count(chr(ord("A") + i)))
    
    # a-z
    for i in range(26):
        result.append(my_string.count(chr(ord("a") + i)))
    
    return result


# 방법 3 (간결)
def solution(my_string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnijk lmnopqrstuvwxyz'
    return [my_string.count(char) for char in alphabet]

def solution(my_string):
    return [my_string.count(alphabet) for alphabet in 
            'abcdefghijklmnopqrstuvwxyz'.upper()+'abcdefghijklmnopqrstuvwxyz']



# [배열 만들기 1]

# 설명
# k의 배수들을 오름차순으로 찾는 문제

# 풀이
# range(k, n+1, k):
#   - 시작: k (k의 첫 배수)
#   - 끝: n+1 (n까지 포함)
#   - 간격: k (k씩 증가)
# k, 2k, 3k, ... 형태로 자동 생성


# 방법 1
def solution(n, k):
    return [i for i in range(k, n+1, k)]


# 방법 2
def solution(n, k):
    return [i for i in range(1, n+1) if n % k == 0]



# [글자 지우기]

# 설명
# indices에 있는 인덱스의 문자들을 제거하는 문제

# 풀이
# 1. 문자열의 각 인덱스를 확인
# 2. i not in indices: 해당 인덱스가 indices에 없으면
# 3. 그 문자를 결과에 추가

# 예시
solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3])
# 인덱스: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# 문자:   a p p o r o o g r a p  e  m  m  e  m  p  r  s
# 제거:   X X     X     X     X  X  X              X
# 남은 문자: p, o, r, o, g, r, a, m, e, r, s
# "programmers"


# 방법 1
def solution(my_string, indices):
    result = ""
    for i in range(len(my_string)):
        if i not in indices:
            result += my_string[i]
    return result


# 방법 2 (리스트 컴프리헨션)
def solution(my_string, indices):
    return ''.join([my_string[i] for i in range(len(my_string)) if i not in indices])


# 방법 3 (set 사용, 효율적임)

def solution(my_string, indices):
    indices_set = set(indices) # set(indices): 리스트를 집합으로 변환, in 연산이 리스트보다 집합에서 훨씬 빠름
    return ''.join([my_string[i] for i in range(len(my_string)) if i not in indices_set])



# [카운트 다운]

# 설명
# start_num부터 end_num까지 1씩 감소하는 리스트를 만드는 문제

# 풀이
# range(start_num, end_num-1, -1):
#   시작: start_num
#   끝: end_num - 1 (end_num을 포함하려면 -1 필요) * 주의해야함!!
#       예시) 10부터 5까지 출력하고 싶다면 range(10, 4, -1)
#   간격: -1 (1씩 감소)


# 방법 1
def solution(start_num, end_num):
    return list(range(start_num, end_num-1, -1))


# 방법 2 (반복문)
def solution(start_num, end_num):
    result = []
    for i in range(start_num, end_num-1, -1):
        result.append[i]
    return result


# 방법 3 (리스트 컴프리헨션)
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num-1, -1)]



# [가까운 1 찾기]

# 설명
# idx보다 큰 인덱스 중에서 값이 1인 가장 작은 인덱스를 찾는 문제

# 풀이
# range(idx, len(arr)): idx부터 배열 끝까지 탐색
# arr[i] == 1:값이 1인 인덱스를 찾으면
# 즉시 그 인덱스 반환 (가장 작은 인덱스)
# 못 찾으면 -1 반환

#예시
solution([0, 0, 0, 1], 1)
# idx=1부터 탐색: arr[1]=0, arr[2]=0, arr[3]=1
# 인덱스 3에서 1 발견
# 3

solution([1, 0, 0, 1, 0, 0], 4)
# idx=4부터 탐색: arr[4]=0, arr[5]=0
# 1을 찾지 못함
# -1

solution([1, 1, 1, 1, 0], 3)
# idx=3부터 탐색: arr[3]=1
# 인덱스 3에서 1 발견
# 3


# 방법 1
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1


# 방법 2 (조건식 활용)
def solution(arr, idx):
    try:
        return arr.index(1, idx) # arr.index(1, idx): idx부터 시작해서 값이 1인 첫번째 인덱스 반환
    except ValueError: # 못 찾으면 ValueError 발생 -> -1 반환
        return -1
    

# 방법 3 (리스트 컴프리헨션)
def solution(arr, idx):
    result = [i for i in range(idx, len(arr)) if arr[i] == 1]
    return result[0] if result else -1
