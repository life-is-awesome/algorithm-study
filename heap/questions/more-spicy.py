'''
문제: https://programmers.co.kr/learn/courses/30/lessons/42626
시간 복잡도: O(n lon n)
풀이 설명:
입력 값을 heapq화 하고, heappush, heappop 연산으로 매운 맛을 올려나간다.
'''

import heapq

def solution(scoville, K):
    answer = 0

    # scoville 배열 heapify - O(n log n)
    heapq.heapify(scoville)

    # 가장 낮은 스코빌 지수가 K 보다 작은 동안
    while scoville[0] < K:

        # 음식이 한 개만 남았다면 불가능
        if len(scoville) == 1:
            return -1

        # 가장 안 매운 음식과 그 다음 안매운 음식 - O(log n)
        first, second = heapq.heappop(scoville), heapq.heappop(scoville)

        # 음식 조합하고 count += 1 - O(log n)
        heapq.heappush(scoville, first + (second * 2))
        answer += 1
    return answer