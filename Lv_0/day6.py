# 20251125

# [마지막 두 원소]

def solution(num_list):
    last = num_list[-1]        # 마지막 원소
    second_last = num_list[-2] # 마지막 바로 전 원소

    # 마지막이 더 크면 (last - second_last) 추가,
    # 크지 않으면 (last * 2) 추가
    if last > second_last:
        num_list.append(last - second_last)
    else:
        num_list.append(last * 2)

    return num_list            # 수정된 리스트 반환



# [수 조작하기 1]

def solution(n, control):
    # control 문자열을 한 글자씩 순서대로 처리
    for c in control:
        if c == "w":      # n + 1
            n += 1
        elif c == "s":    # n - 1
            n -= 1
        elif c == "d":    # n + 10
            n += 10
        elif c == "a":    # n - 10
            n -= 10
    
    return n  # 모든 조작 이후의 최종값

# [수 조작하기 2]

def solution(numLog):
    answer = ""
    
    # numLog[0] → 시작값
    # numLog[i] - numLog[i-1] → 한 번의 조작으로 얼마나 변했는지 계산
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        
        # 변화량에 따라 어떤 키를 눌렀는지 판별
        if diff == 1:        # +1 → w
            answer += "w"
        elif diff == -1:     # -1 → s
            answer += "s"
        elif diff == 10:     # +10 → d
            answer += "d"
        elif diff == -10:    # -10 → a
            answer += "a"
        else:
            pass  # 문제 조건상 올 일 없음
            
    return answer