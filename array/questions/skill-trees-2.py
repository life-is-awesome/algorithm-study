'''
문제: https://programmers.co.kr/learn/courses/30/lessons/49993
시간 복잡도: O(mn)
풀이 설명:
자주 참조해야할 skill 은 집합화하고, 필터링 + 비교
(1번 풀이에서 필터를 이용한 간소화)
'''
def solution(skill, skill_trees):
    answer = 0

    # 선행 트리 체커를 생성한다. - O(n)|n = len(skill)
    skill_checker = set(skill)

    # 모든 스킬 트리를 순회하면서
    for skill_tree in skill_trees:
        # 선행 스킬이 아닌거는 걸러내고
        req_skills = ''.join(\
                filter(lambda x: x in skill_checker, skill_tree))
        # 걸러낸 스킬이 선행 스킬에 반하지 않으면 ++
        if req_skills == skill[:len(req_skills)]:
            answer += 1
    # 위 반복문의 시간 복잡도는
    # O(nm)|n=len(skill_trees), m=[각 skill_tree 의 평균 문자 개수]
    return answer