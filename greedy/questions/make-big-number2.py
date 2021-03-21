'''
문제: https://programmers.co.kr/learn/courses/30/lessons/42883
시간 복잡도: O(n)
풀이 설명:
1. number 배열을 하나씩 answer로 복사한다.
2. number 에서 answer로 복사할 때, 가장 마지막에 복사한 값이 현재 복사하는
  값보다 작다면 제거한다.
    -> 가장 높은 자리에서 뒤보다 작은 수를 제거함으로써 현재 상태에서 하나
      를 제거했을 때 가장 큰 수가 남게 된다.
3-1. 1~2 를 반복하여 제거한 수가 k 가 되면, 복사하지 않은 모든 수를 한번에 복사한다.
3-2. 모든 수를 복사했을 때 제거한 수가 k 보다 적다면 뒤에서부터 남은 개수를 제거한다.
  -> 모든 복사를 마치면 뒤에 있는 수는 반드시 앞에 있는 수 보다 작거나 닽다.
'''

def solution(number, k):
    answer = []

    for i, n in enumerate(number):
        # 이전에 append 된 마지막 숫자가 현재보다 클때까지 제거
        while answer and answer[-1] < n:
            answer.pop()
            k += 1

            # k개 제거하면 반환
            if k == k:
                return ''.join(answer + list(number[i:]))

        # 현재 값을 append
        answer.append(n)

    return ''.join(answer[:-k])