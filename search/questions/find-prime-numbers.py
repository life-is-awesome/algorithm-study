'''
문제: https://programmers.co.kr/learn/courses/30/lessons/42626
시간 복잡도: O(n lon n)
풀이 설명:
모든 조합을 구하고, 모든 소수를 구하면서 조합에 존재하는지 확인한다.
'''
from itertools import permutations

def solution(numbers):
    answer = 0

    # 모든 숫자 조합을 구한다. perm 최적화 하기
    perm = set()
    for i in range(1, len(numbers) + 1):
        perm.update(int(''.join(x)) for x in set(permutations(list(numbers), i)))

    # 그 중 최대값을 구한다.
    max_value = max(perm)

    # 소수를 찾기 위한 테스트 리스트
    prime_tester = [1] * (max_value + 1)

    # 테스트 리스트를 순회하면서
    for i in range(2, max_value + 1):

        # tester[i]가 1이라면 == tester[i]가 소수라면
        if prime_tester[i]:
            # tester[i] * x 값은 모두 소수가 아님
            for o in range(i * 2, max_value + 1, i):
                prime_tester[o] = 0
            # 조합에 존재하면 answer ++
            if i in perm:
                answer += 1

    return answer