# 분수의 덧셈

# import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    # 수도코드
    # 분수의 덧셈
    # 1. 분모를 맞춰준다. (분자 덧셈 할 수 있게)
    # 2. 분모 맞춰줄 때 사용한 값을 각 분자에 곱해준다.
    # 3. 분자를 더한다.
    head = numer1 * denom2 + numer2 * denom1 # 분자
    body = denom1 * denom2 # 분모
    # print(head, body)
    # 1 / 2 -> 4 / 8
    # 3 / 4 -> 6 / 8
    # -> 10 / 8
    
    # 기약분수
    # 1. 최대공약수로 나눠준다.
    # temp = math.gcd(head, body) # 0.01ms
    # print(temp)
    # 반복문 통해서 최대공약수 확인 # 61 ms
    # 두 값을 나눌 수 있는 가장 큰 값
    # 둘 중에 작은 값까지만 확인
    for i in range(1, min(head, body) + 1):
        # 여기서 두 값이 나눠지는지 체크
        if head % i == 0 and body % i == 0:
            # 둘 다 나눠 떨어지면, 최대공약수로 바꿔줌
            temp = i
    
    # list comprehension # 101 ms
    # temp = [i for i in range(1, min(head, body) + 1) if head % i == 0 and body % i == 0][-1]
    
    answer = [head//temp, body//temp]
    return answer

# 모듈을 import 해서 사용할 때와, 그냥 실행할 때 차이
from module import hello_print

if __name__ == '__main__':
    hello_print()
    print(solution(9, 2, 1, 3) == [29, 6])
