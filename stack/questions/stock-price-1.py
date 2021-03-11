'''
풀이 시간: X
문제: https://programmers.co.kr/learn/courses/30/lessons/42584
시간 복잡도: O(n²)
풀이 설명:
Brute-Force 형식의 풀이
'''
def solution(prices):
    # 정답을 저장할 별도의 리스트를 초기화 한다. - 시간 복잡도 O(n)
    ans = [-1] * len(prices)

    # 주어진 가격의 첫 인자부터 순회하면서
    for i, crit in enumerate(prices):
        # 주어진 가격 crit 보다 작은 가격이 있으면 위치 차이를 ans 에 저장한다.
        for o in range(i + 1, len(prices)):
            if prices[o] < crit:
                ans[i] = o - i
                break

        # 내부 순회를 마쳤을 때 ans 값이 변하지 않았다면 마지막까지 가격이 떨어지지 않은 경우이다.
        if ans[i] == -1:
            ans[i] = len(prices) - i - 1
    # 위 순회문의 시간 복잡도는 최악의 경우 n + (n - 1) + ... 1 이므로 O(n²) 이다.

    # 완성된 ans를 반환한다.
    return ans