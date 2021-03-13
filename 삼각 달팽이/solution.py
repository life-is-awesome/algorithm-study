'''
풀이 시간: X
문제: https://programmers.co.kr/learn/courses/30/lessons/68645
시간 복잡도: O(n²)
풀이 설명:
이차원 배열 형식으로 삼각형을 만들고, 모든 삼각형 원소들에대해 순회하며 값을 입력한다.
'''
import sys

def solution(n):
    firsts = [[-1] * (i + 1) for i in range(n)]
    g = (x for x in range(1, sys.maxsize))
    row = col = 0

    firsts[row][col] = next(g)
    while True:
        if not (row + 1 < n and firsts[row + 1][col] == -1): break
        while row + 1 < n and firsts[row + 1][col] == -1:
            row += 1
            firsts[row][col] = next(g)
        while col + 1 < n and firsts[row][col + 1] == -1:
            col += 1
            firsts[row][col] = next(g)
        while col - 1 < n and row - 1 < n and firsts[row - 1][col - 1] == -1:
            col -= 1
            row -= 1
            firsts[row][col] = next(g)

    ret = []
    for li in firsts:
        ret += li
    return ret