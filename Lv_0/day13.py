# 20251221

# [n 번째 원소부터]

# 주의할점
# 일반적으로 "n번째 원소"는 인덱스 n-1을 의미
# 1번째 = 인덱스 0, 2번째 = 인덱스 1

def solution(num_list, n):
    return num_list[n-1:]



# [순서 바꾸기]

# 설명
# 리스트를 n번째 원소를 기준으로 나누고
# 뒷부분을 앞부분 앞에 붙이는 문제

# 핵심
# - num_list[:n]: n번째까지(0부터 n-1까지)
# - num_list[n:]: n번째 이후(n부터 끝까지)


def solution(num_list, n):
    return num_list[n:] + num_list[:n]



# [왼쪽 오른쪽]

# 설명
# "l"와 "r"중 먼저 나오는 것 찾기
# l이 먼저면 -> 왼쪽 부분 반환
# r이 먼저면 -> 오른쪽 부분 반환
# 둘 다 없으면 빈 리스트 반환

def solution(str_list):
    for i, s in enumerate(str_list):
        if s == "l":
            return str_list[:i]
        elif s == "r":
            return str_list[i+1:]
        
    return []

# 핵심
# - str_list[:i] : i번째 앞쪽(왼쪽)
# - str_list[i+1:] : i번째 뒤쪽(오른쪽)
# 반복문으로 순회하면 자동으로 먼저 나오는 것을 찾음



# [n번째 원소까지]

# 핵심
# num_list[:n]: 처음부터 n번째까지
#   - 1번째 = 인덱스 0
#   - n번쨰 = 인덱스 n-1
#   - 슬라이싱 [::n]은 인덱스 0부터 n-1까지 포함


def solution(num_list, n):
    return num_list[:n]



# [n개 간격의 원소들]

# 설명
# num_list[start:end:step]
#   - start부터 end-1까지 step간격으로
#   - 처음부터 끝까지 n간격이므로 -> [::n]

def solution(num_list, n):
    return num_list[::n]