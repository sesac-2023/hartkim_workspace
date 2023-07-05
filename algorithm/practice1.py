def solution(numbers):
#     answer = []
#     # 배열의 요소들을 하나씩 순회한다.
#     for number in numbers:
#         answer.append(number * 2) # 2배하고 answer에 담아줌

#     return answer

    # 1. map(함수, 배열) -> 배열의 요소들을 하나씩 함수에서 넣어서 결과를 반환
    # 2배 해주는 함수
    def func(x):
        return x * 2
    # lambda x: x * 2 -> 한 줄 함수 표현식
    # print(map(func, numbers))
    # return list(map(func, numbers))

    # return list(map(lambda x : x * 2, numbers))
    # 2. list comprehension
    return [number * 2 for number in numbers]

if  __name__ == '__main__':
    solution([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]