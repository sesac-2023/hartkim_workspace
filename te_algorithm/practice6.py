# 짝수 홀수 개수 세기
def solution(num_list):
    answer = []
    # 접근 방법
    # 개수를 세어야 하니까
    # 지금까지 센 개수를 저장해둘 어떤 변수가 필요하다.
    even = 0
    odd = 0
    
    # num_list의 숫자를 하나씩 꺼내보면서, -> 반복문
    for number in num_list:
        # 짝수인지,
        if number%2 == 0:
            even += 1
        # 홀수인지
        elif number%2 == 1:
            odd += 1
    
    # 개수 센 것을 짝수, 홀수 순으로 answer에 담아준다.
    answer = [even, odd]
    return answer

def solution(num_list):
    answer = [0, 0] # 짝수, 홀수
    
    for number in num_list:
        if number%2 == 0:
            answer[0] += 1
        elif number%2 == 1:
            answer[1] += 1

    return answer

def solution(num_list):
    # list comprehension
    # sum([1 for number in num_list if number%2 == 0])
    return [len([number for number in num_list if number%2 == 0]), 
            len([number for number in num_list if number%2 == 1])]
