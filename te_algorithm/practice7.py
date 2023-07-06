# 옷가게 할인 받기
def solution(price):
    answer = 0
    # price = 80000 이라면?
    discount = 0
    
    # 100050 -> int(5,002.5) 95048
    # 100050 - 5,002.5 -> int(95047.5) -> 95047

    # 10만원 이상이면, 5% 할인
    if price >= 100000:
        discount = price * 0.05
    
    # 30만원 이상이면, 10% 할인
    if price >= 300000:
        discount = price * 0.1
    
    # 50만원 이상이면, 20% 할인
    if price >= 500000:
        discount = price * 0.2
    
    return int(price - discount)


def solution(price):
    answer = 0

    discount = 0
    # price = 50000
    # price = 150000
    # price = 450000
    # price = 550000

    # 중첩된 조건문을 사용할 때에는, 값의 포함여부를 잘 체크하자
    if price >= 500000:
        discount = price * 0.2
    elif price >= 300000:
        discount = price * 0.1
    elif price >= 100000:
        discount = price * 0.05

    return int(price - discount)

def solution(price):
    answer = price

    if price >= 500000:
        # discount = price * 0.2 # 할인되는 금액
        answer = price * 0.8 # -> 내가 지불해야하는 금액
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95

    return int(answer)

def solution(price):
    # 조건 표현식 : <참일 때 값> if 조건식 else <거짓일 때 값>
    # elif를 강제로 넣는다면?
    # <elif일 때 값> ?
    # <참일 때 값> if 조건식 <elif일 때 값> elif 조건식 else <거짓일 때 값>
    # price * 0.8 if price >= 500000 elif price >= 300000 price * 0.9 else price * 0.95

    answer = price * 0.8 if price >= 500000 else \
                price * 0.9 if price >= 300000 else \
                price * 0.95 if price >= 100000 else price
    
    return int(answer)
