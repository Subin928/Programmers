# 20251125 20251126

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
