# day 1

# [대소문자 바꿔서 출력하기]

str = input()
print(str.swapcase())   # 대소문자 바꾸기 코드 .swapcase()

# [특수문자 출력하기]

print("!@#%^&*(\\`\"<>?:;") # 첫 번째 방법 : \ -> \\ , " -> \" , ` -> `
print(r'!@#$%^&*(\'"<>?:;') # 두 번째 방법 : r만 붙이는 경우도 있음



# day 2

# [문자열 붙여서 출력하기]

# 두 개의 문자열이 공백으로 구분되어 입력으로 주어질떄

str1, str2 = input().strip().split('')
print(str1, str2, sep='')      # -> sep=' ' : 기본값(공백), sep='' : 사이에 아무것도 넣지 않음(붙여쓰기)

# [문자열 돌리기]

# 문자열 str을 시계방향으로 90도 돌려서 아래로 입출력

str = input()
for ch in str:
    print(ch)

# [문자열 겹쳐쓰기(어려움)]

# 문자열 my_string, overwrite_string과 정수 s가 주어질때 문자열 my_string의 인덱스 s부터 
# overwrite_string의 길이만큼을 문자열 overwrite_string으로 바꾼 문자열을 return하는 함수

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]



# day 3

# [문자열 섞기]

# 길이가 같은 두 문자열 str1, str2 서로 번갈아가면서 등장하게

def solution(str1, str2):
    result = ""
    for a, b in zip(str1, str2):   # -> zip : 각 문자열에서 같은 위치의 문자끼리 한 쌍으로 묶는 함수 : zip(str1, str2)
        result += a + b
    return result

# [문자 리스트를 문자열로 변환하기]

# 문자들이 담겨있는 배열 arr가 주어진다. arr의 원소들을 순서대로 이어붙인 문자열 return하는 함수

def solution(arr):
    return "".join(arr)       # "".join() : ()안의 모든 문자열을 붙여 하나의 문자열로 만들기

# [더 크게 합치기]

# 연산 +는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환

def solution(a, b):
    answer = 0
    return max(int(str(a)+str(b)), int(str(b)+str(a)))  # max(a, b) : a, b 중 더 큰 값을 골라서 반환



# day 4

# [n의 배수]

# 정수 num과 n이 매개 변수로 주어질때, num이 n의 배수이면 1, 아니면 0 return하는 함수

def solution(num, n):
    return 1 if num % n ==0 else 0

# [홀짝에 따라 다른 값 반환하기]

# n이 홀수라면 n 이하의 홀수인 모든 양의 정수 합 return
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수 제곱의 합 return

def solution(n):
    if n % 2 == 1:
        return sum(i for i in range(1,n+1,2))
    else:
        return sum(i**2 for i in range(2,n+1,2)) # 첫 번째 방법
    
def solution(n):
    answer = 0              # answer = 0은 숫자를 더할 준비하는 단계 / answer=""는 문자열을 이어붙일 준비
    if n % 2:
        for i in range(1,n+1,2):
            answer +=  i

    else:
        for i in range(2,n+1,2):
            answer += i **2

    return answer                                # 두 번째 방법

# [flag에 따라 다른 값 반환하기]

# flag가 true이면 a+b를, false면 a-b를 return하는 함수

def solution(a, b, flag):
    if flag:               # if flag : flag가 True이면 실행 O / falg가 False이면 실행 X
        return a + b
    else:
        return a - b