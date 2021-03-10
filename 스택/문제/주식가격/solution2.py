'''
풀이 시간: X
문제: https://programmers.co.kr/learn/courses/30/lessons/42584
시간 복잡도: O(n)
풀이 설명:
solution 1 로 부터 시/공간 복잡도를 최적화 해본 풀이
- 스택을 이용한 상태 저장으로 시간 복잡도 최적화
- ans 대신 prices에 결과를 직접 업데이트하여 공간 복잡도 최적화
'''

def solution(prices):
    # 상태를 저장할 스택
    # (i, p) → i: prices 에서의 인덱스 / p: prices[i]
    # 스택에서 뒤 쪽의 i 은 앞쪽의 i 보다 항상 작다.
    # 스택에서 뒤 쪽의 p 는 앞쪽의 p 보다 항상 크다.
    stack = []

    # 주어진 가격의 마지막 인자부터 순회하면서
    for i in range(len(prices) - 1, -1, -1):

        # 스택에 있는 현재 가격보다 비싼 가격들을 pop 한 후
        while stack and stack[-1][1] >= prices[i]:
            stack.pop()

        # 스택이 비어있으면 → 현재 가격은 마지막 까지 떨어지지 않는다.
        # ∵ 현재 가격 보다 비싼 가격을 stack 에서 모두 pop 했으므로
        # ∴ ans 에 마지막까지 걸리는 시간을 저장한다.
        if not stack:
            ans = len(prices) - i - 1

        # 스택이 비어있지 않으면 → 스택의 마지막 인자는 가격이 떨어지는 가장 가까운 위치다.
        # ∴ ans 에 가격이 떨어지는 시간을 저장한다.
        else:
            ans = stack[-1][0] - i

        # 처리한 위치와 가격을 스택에 push 하고, prices 에 가격이 떨어지는 시간을 set 한다.
        stack.append((i, prices[i]))
        prices[i] = ans
    '''
    위 순회문의 시간 복잡도는 O(n) 이다.
        1. {19}줄의 반복문의 시간복잡도() - O(n)
        2. stack 에 push, pop 하는 시간 복잡도({22}줄, {37}줄) - O(n)
            - stack 에 push, pop 하는 연산은 prices 의 인자들에 대해서만 수행한다.
            - prices 의 인자의 개수는 n 이다.
            - push 는 최대 n 번, pop 은 최대 n 번으로 연산은 최대 2n 번 발생한다. - O(n)
    '''

    # 완성된 prices를 반환한다.
    return prices