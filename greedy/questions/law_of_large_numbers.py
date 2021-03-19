'''
문제: 큰 수의 법칙
설명: N, M, K 3가지의 숫자를 공백으로 받는다. N은 배열 길이, M은 총 연산 횟수, K번 이상 초과하여 가장 큰 수를 연산할 수 없다. 배열의 값은 랜덤으로 중복 포함하여 주어진다.
     가장 큰 수의 조합이 나올 수 있도록 구현하기
예시: 3, 4, 3 & [1, 4, 6, 1] 일때 6+6+6+4 = 22 가 나와야 한다.
'''
n, m, k = map(int, input().split())
data_list = list(map(int, input().split()))
data_list.sort(reverse=True)  # 내림차순 정렬

result = 0
first_no = data_list[0]  # 가장 큰 수
second_no = data_list[1]  # 두번째 큰 수

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_no
        m = m - 1  # 해당 연산 횟수를 -로 차감
    if m == 0:
        break
    result += second_no
    m = m - 1  # 연산이후엔 꼭 횟수 - 차감

print(result)
