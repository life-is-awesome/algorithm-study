'''
풀이 시간: X
문제: https://programmers.co.kr/learn/courses/30/lessons/42860#
시간 복잡도: O(n)
풀이 설명:
1 번 순회하면서 필요한 정보들을 업데이트 한다.
'''
def solution(name):
    # 시간 복접도 절약을 위해 그냥 선언해 버리자
    m = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,\
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8,\
         'T': 7, 'U': 6, 'V': 5, 'W': 4, 'X': 3, 'Y': 2, 'Z': 1}

    count = 0
    # 연속으로 나오는 'A' 중 가장긴 (길이, 시작점, 끝점)
    max_continue_a = (-1, -1, -1)
    start_a = end_a = -1

    for i, ch in enumerate(name):
        # 여기는 카운트 세는곳
        if ch != 'A':
            count += m[ch]

        # 아래 조건들은 'A' 체크 하는 곳
        elif end_a < i:
            max_continue_a = max(max_continue_a,\
                                 (end_a - start_a, start_a, end_a), key=lambda x: x[0])
            start_a = i
            end_a = i + 1
        elif end_a == i:
            end_a += 1

    # 마무리 체크
    max_continue_a = max(max_continue_a,\
                         (end_a - start_a, start_a, end_a), key=lambda x: x[0])

    # 전부 'A'면 0
    if count == 0: return 0

    # 'A'가 하나도 없으면 전체를 조이스틱 이동
    elif start_a == -1: return count + len(name) - 1

    # 가장 긴 'A'가 마지막 쪽에 있으면 가장 긴 'A' 시작전까지
    elif max_continue_a[2] >= len(name): return count + max_continue_a[1] - 1

    # 그 외에는 일직선으로 했을 때 vs 가장 긴 'A' 전에 뒤돌아가서 순회 중 짧은거로
    else: return count + min(len(name) - 1, \
                             (max_continue_a[1] - 1) * 2 + len(name) - max_continue_a[2])