# 20251206 20251207

# [간단한 논리 연산]

# 문제 이해
# (x1 ∨ x2) ∧ (x3 ∨ x4)를 계산

def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)


# [주사위 게임 3]

# 1. 4개 같음 (p, p, p, p) -> 1111 x p
# 2. 3개 같음 (p, p, p, p) -> (10 x p + q)^2
# 3. 2개씩 같음 (p, p, p, q) -> (p + q) * |p - q|
# 4. 2개 같음 (p, p, q, r) -> q * r
# 5. 모두 다름 -> 가장 작은 수

def solution (a, b, c, d):
    from collections import Counter

    # 각 숫자의 등장 횟수 세기
    dice = [a, b, c, d]
    count = Counter(dice) # {숫자: 개수} 딕셔너리
    counts = sorted(count.values(), reverse=True) # 개수만 추출해서 내림차순
                                                  # [4] or [3,1] or [2,2] or [2,1,1] or [1,1,1,1]

    # 1. 네 주사위 모두 같음 (4개)
    if counts == [4]:
        p = a
        return 1111 * p
    
    # 2. 세 주사위 같음 (3개, 1개)
    elif counts == [3, 1]:
        p = [num for num, cnt in count.items() if cnt == 3][0]
        q = [num for num, cnt in count.items() if cnt == 1][0]

    # 3. 두 개씩 같음 (2개, 2개)
    elif counts == [2, 2]:
        nums = [num for num, cnt in count.items() if cnt == 2]
        p, q = nums[0]. nums[1]
        return (p + q) * abs(p - q)
    
    # 4. 두 주사위만 같음 (2개, 1개, 1개)
    elif counts == [2, 1, 1]:
        p = [num for num, cnt in count.items() if cnt == 2][0]
        others = [num for num, cnt in count.items() if cnt == 1]
        q, r = others[0], others[1]
        return q * r
    
    # 5. 모두 다름 (1개, 1개, 1개, 1개)
    else:
        return min(dice)

# <Counter 이해하기>

from collections import Counter

dice = [3, 3, 3, 5]
count = Counter(dice)
print(count) # Counter({3: 3, 5: 1})

# 개수만 추출
counts = sorted(count.values(), reverse=True)
print(counts)

# 3번 나온 숫자 찾기
p = [num for num, cnt in count.items() if cnt == 3][0]
print(p) # 3


# <counter 없이 풀이>

def solution(a, b, c, d):
    dice = [a, b, c, d]

    # 각 숫자의 등장 획수를 딕셔너리로 세기
    count_dict = {}
    for num in dice:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # 등장 횟수만 추출해서 정렬
    counts = sorted(count_dict.values(), reverse = True)

    # 1. 네 주사위 모두 같음 (4개)
    if counts == [4]:
        return 1111 * a
    
    # 2. 세 주사위 같음 (3개, 1개)
    elif counts == [3, 1]:
        p = [num for num, cnt in count_dict.items() if cnt == 3][0]
        q = [num for num, cnt in count_dict.items() if cnt == 1][0]

    # 3. 두 개씩 같음  (2개, 2개)
    elif counts == [2, 2]:
        nums = [num for num, cnt in count_dict.items() if cnt == 2]
        p, q = nums[0], nums[1]
        return (p + q) * abs(p - q)
    
    # 4. 두 주사위만 같음 (2개, 1개, 1개)
    elif counts == [2, 1, 1]:
        p = [num for num, cnt in count_dict.items() if cnt == 2][0]
        others = [num for num, cnt in count_dict.items() if cnt == 1]
        q, r = others[0], others[1]
        return q * r
    
    # 5. 모두 다름 (1개, 1개, 1개, 1개)
    else:
        return min(dice)


# <sorted 활용 풀이>

def solution(a, b, c, d):
    dice = sorted([a, b, c, d])

    # 1. 모두 같음
    if dice[0] == dice[3]:
        return 1111 * dice[0]
    
    # 2. 3개 같음
    elif dice[0] == dice[2]: # [p, p, p, q]
        return (10 * dice[0] + dice[3]) ** 2
    elif dice[1] == dice[3]: # [q, p, p, p]
        return (10 * dice[1] + dice[0]) ** 2
    
    # 3. 2개씩 같음
    elif dice[0] == dice[1] and dice[2] == dice[3]:  # [p, p, q, q]
        return(dice[0] + dice[2])
    
    # 4. 2개만 같음
    elif dice[0] == dice[1]:         # [p, p, q, r]
        return dice[2] * dice[3]
    elif dice[1] == dice[2]:         # [q, p, p, r]
        return dice[0] * dice[3]
    elif dice[2] == dice[3]:         # [q, r, p, p]
        return dice[0] * dice[1]
    
    # 5. 모두 다름
    else:
        return dice[0]
    


# <프로그래머스 정답>


def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)



# [글자 이어 붙여 문자열 만들기]

# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. 
# my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 
# 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.


# 방법 1. 리스트 컴프리헨션 + join
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])

# 방법 2. for 루프.
def solution(my_string, index_list):
    result = ''
    for i in index_list:
        result += my_string[i]
    return result

# 방법 3. map 사용
def solution(my_string, index_list):
    return ''.join(map(lambda i: my_string[i], index_list))

# 핵심 포인트
# 1. 인덱싱 : my_string[i]로 특정 위치의 문자 가져오기
# 2. 리스트 컴프리헨션 : [my_string[i] for i in index_list]
# 3. join : 리스트의 문자들을 하나의 문자열로 합치기

# 예시
my_string = "hello"
index_list = [1, 4, 0, 0, 3]


my_string[3] = 'l'# 1단계
my_string[1] = 'e'
my_string[4] = 'o'
my_string[0] = 'h'
my_string[0] = 'h'

# 2단계 : 리스트로 만들기
chars = ['e', 'o', 'h', 'h', 'l']

# 3단계 : 문자열로 합치기
result = ''.join(chars) # eohhl



# [9로 나눈 나머지]

# 문제 이해
# 핵심 원리: 숫자를 9로 나눈 나머지 = 각 자릿수의 합을 9로 나눈 나머지
# 예시: 123 % 9 = (1+2+3) % 9


# 방법 1: 각 자릿수 합 구하기
def solution(number):
    digit_sum = sum(int(digit) for digit in number)
    return digit_sum % 9

# 방법 2: 한 줄로
def solution(number):
    return sum(int(d) for d in number) % 9

# 방법 3: for 루프
def solution(number):
    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)
    return digit_sum % 9

# 방법 4: 직접 계산(매우 큰 숫자에서는 느릴 수 있기 때문에 권장x)

def solution(number):
    return int(number) % 9


# 핵심 포인트
# 1. 문자열 -> 숫자 변환 : int(digit)
# 2. 제너레이터 표현식 : (int(d) for d in number)
# 3. sum()함수 : 자동으로 모든 값을 더함
# 4. 나머지 연산: % 9



# [문자열 여러 번 뒤집기]

# 문제 이해
# 문자열의 특정 구간을 여러 번 뒤집기


#  방법 1. 슬라이싱 활용

def solution(my_string, queries):
    my_string = list(my_string)   # 문자열을 리스트로 변환

    for s, e in queries:
        # s부터 e까지 구간을 뒤집기
        my_string[s:e+1] = my_string[s:e+1][::-1]

    return ''.join(my_string)


# 방법 2. reverse() 사용

def solution(my_string, queries):
    my_string = list(my_string)

    for s, e in queries:
        # s부터 e까지 부분 리스트 추
        part = my_string[s:e+1]
        # 뒤집기
        part.reverse()
        # 다시 넣기
        my_string[s:e+1] = part
    
    return ''.join(my_string)


# 핵심 포인트
# 1. 문자열은 불변 : 리스트로 변환해야 수정 가능
# 2. 슬라이싱 : [s, e+1]로 s부터 e까지(e 포함!)
# 3. 역순 [::-1]로 뒤집기
# 4. join: 리스트를 다시 문자열로


# 예시

s = "abcde"
s_list = list(s)   # ['a', 'b', 'c', 'd', 'e']

# 인덱스 1~3 뒤집기
s_list[1:4] = s_list[1:4][::-1]

# s_list[1:4] = ['b', 'c', 'd']
# s_list[1:4][::-1] = ['d', 'c', 'b']

result = ''.join(s_list)  # "abcde"
