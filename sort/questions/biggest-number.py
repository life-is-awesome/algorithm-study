from functools import cmp_to_key

# 비교 함수
def compare(a, b):
    a, b = a + b, b + a

    # a 가 앞에 있을 때 사전상 빠르면 1
    if a < b:
        return 1

    # b 가 앞에 있을 때 사전상 빠르면 -1
    elif a > b:
        return -1

    # 둘이 같다면 0
    return 0

def solution(numbers):
    # numbers 를 문자열화 하고 비교 함수로 정렬한 뒤 이어붙인다.
    answer = ''.join(sorted([str(x) for x in numbers], key=cmp_to_key(compare)))

    # 0으로 시작한다면 모든 숫자가 0 이므로, "0"을 반환한다.
    return answer if answer[0] != "0" else "0"