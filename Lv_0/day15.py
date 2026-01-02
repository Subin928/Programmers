# 20260102

# [조건에 맞게 수열 변환하기]

# 문제이해
# 50 이상의 짝수 -> 2로 나누기
# 50 미만의 홀수 -> 2 곱하기
# 나머지는 그대로 유지

def solution(arr):
    answer = []

    for num in arr:
        if num >= 50 and num % 2 == 0:
            answer.append(num // 2)
        elif num < 50 and num % 2 == 1:
            answer.append(num * 2)
        else:
            answer.append(num)
    return answer



# [조건에 맞게 수열 변환하기 2]

# 문제이해
# 50 이상의 짝수 -> 2로 나누기
# 50 미만의 홀수 -> 2 곱하기
# 나머지는 그대로 유지
# 이 변환을 반복하다가 배열이 변하지 않으면 그때까지의 횟수를 반환

def solution(arr):
    x = 0

    while True:
        new_arr = []

        for num in arr:
            if num >= 50 and num % 2 == 0:
                new_arr.append(num // 2)
            elif num < 50 and num % 2 == 1:
                new_arr.append(num * 2 + 1)
            else:
                new_arr.append(num)

        if arr == new_arr:
            return x
        
        arr = new_arr
        x += 1

# 핵심 로직:
# 1. 배열을 변환해서 new_arr에 저장
# 2. 원래 배열(arr)과 비교
# 3. 같으면 x 반환, 다르면 계속 반복