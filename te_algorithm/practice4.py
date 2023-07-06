# 피자 나눠먹기 1 ~ 3

# 피자 1
import math
def solution(n):
    answer = 0
    
    # 피자를 7조각으로 나눠주고,
    # n명이 한 조각 이상씩 먹을 수 있도록 하는 피자의 수
    
    # 15명
    # 7조각 피자
    # 15/7 => 2.142857 판 -> 올림
    # 반올림을 하게되면, 2판 14명은 1조각씩 먹을 수 있고, 1명은 0조각
    answer = math.ceil(n/7)
    
    # 조건식
    if n % 7 != 0: # 사람 수를 7조각으로 나눴을 때, 나머지가 있으면,
        answer = n // 7 + 1 # 한 판을 더 시킨다.
    else: # 7조각으로 나누어 떨어지면,
        answer = n // 7 # 피자 수 그대로 반환
    
    # 조건표현식
    answer = (n // 7 + 1) if n % 7 != 0 else (n // 7 + 0)
    answer = n // 7 + (1 if n % 7 != 0 else 0)
    
    return answer

# 피자 2
def solution(n):
    answer = 0
    
    # 10
    # 한 판 시켰을 때 (6 조각)
    # 6 -> 1
    # 4 -> 0
    
    # 두 판 시켰을 때 (12 조각)
    # 2 -> 2
    # 8 -> 1
    
    # 세 판 시켰을 때 (18 조각)
    # 8 -> 2
    # 2 -> 1
    
    # 네 판 시켰을 때 (24 조각)
    # 4 -> 3
    # 6 -> 2
    
    # 다섯 판 째 (30 조각)
    # 10 -> 3
    
    # 6 * 10 = 6조각씩
    # 피자를 사람 수만큼 시키면, 모두가 6조각씩 먹을 수 있음
    # 이거를 최소로하겠다
    # 6, n의 최소공배수를 구하겠다.
    
    # 최소공배수 찾는 법
    # 1 ~ 60
    # 30 -> 10, 6의 최소공배수 
    # 30/10 => 3, 0 30/6 => 5, 0
    for number in range(1, 6 * n + 1):
        if number % 6 == number % n == 0:
            answer = number // 6
            break
    
    return answer

# 피자 3 
def solution(slice, n):
    answer = 0
    # slice = 7, 피자 1
    
    answer = n//slice+1 if n%slice != 0 else n//slice
    return answer