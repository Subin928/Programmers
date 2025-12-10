# 20251210

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


# 방법 3
def solution(my_string):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnijk lmnopqrstuvwxyz'
    return [my_string.count(char) for char in alphabet]