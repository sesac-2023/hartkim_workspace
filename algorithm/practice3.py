# 최빈값 구하기

def solution(array):
    answer = 0
    counter = {}
    # 1. 빈도수 확인 (배열을 돌면서)
    for number in array:
        counter[number] = counter.get(number, 0) + 1 # 1개 추가
    # 결과
    # counter = {
    #     1: 1,
    #     2: 1, 
    #     3: 3,
    #     4: 1,
    # }
    print(counter)
    
    # 2. 최빈값 개수 확인, 결과값 반환
    
    max_median = -1
    max_values = [] # 빈도수가 같으면, 여기에 넣어주기 위해서
    for key in counter:
        key, counter[key] # 숫자와 빈도수
        if max_median < counter[key]: # 현재 빈도수가 더 크면,
            max_values = [key] # max_values를 key로 초기화
            max_median = counter[key] # 빈도수로 최신화
        elif max_median == counter[key]: # 빈도수가 같으면?
            max_values.append(key) # 값 목록에 추가
    
    if len(max_values) > 1:
        answer = -1
    else:
        answer = max_values[0]
    
    # 조건표현식
    answer = -1 if len(max_values) > 1 else max_values[0]
    
    return answer