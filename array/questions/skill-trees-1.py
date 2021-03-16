'''
문제: https://programmers.co.kr/learn/courses/30/lessons/49993
시간 복잡도: O(n)
풀이 설명:
자주 참조해야할 skill 은 집합화하고, 배열 내 모든 문자열 순회
'''
def solution(skill, skill_trees):
    answer = 0

    # 선행 트리 체커를 생성한다. - O(n)|n = len(skill)
    skill_checker = set(skill)

    # 모든 스킬 트리를 순회하면서
    for skill_tree in skill_trees:
        # 배울 수 있는 선행 스킬 위치 초기화
        skill_p = 0
        is_valid = True

        # 스킬들을 순회하면서
        for s in skill_tree:
            # 선행 스킬이 끝나면 무조건 가능
            if skill_p >= len(skill):
                break
            # 배울 수 있는 선행 스킬이 오면 다음 선행 스킬을 가리킴
            elif s == skill[skill_p]:
                skill_p += 1
            # 배울 수 없는 선행 스킬이 나오면 유효하지 않음
            elif s in skill_checker:
                is_valid = False
                break
        if is_valid: answer += 1
    # 위 반복문의 시간 복잡도는 O(n)|n=[skill_trees 내의 문자 개수 총합]

    return answer
