'''
문제: https://programmers.co.kr/learn/courses/30/lessons/42883
시간 복잡도: O(n²)
풀이 설명:
- 사실 알고리즘 자체는 O(n) 시간 복잡도로 보이지만, 실제로 pop(x)는 파이썬
리스트 특성상 평균 O(n)의 시간복잡도를 갖기 때문에 전체 시간 복잡도는 O(n²)
이 된다.
- 마지막으로 제거된 원소 이전 부터 비교하여 다음 수 보다 작은 수들을 k개
제거하고, 순회를 마치면 k 중 남은 개수를 추가 제거한다.
'''
def solution(number, k):
    number = list(number)

    last_p = 0

    # k 번 동안
    for _ in range(k):

        # number 의 마지막 전까지
        for i in range(last_p, len(number) - 1):

            # 뒤 숫자보다 작은 숫자가 있으면 제거 - 평균 O(n)
            if number[i] < number[i + 1]:
                number.pop(i)
                break
            elif i == len(number) - 2:
                number.pop()
            last_p = i - (1 if i != 0 else 0)

    return ''.join(number)