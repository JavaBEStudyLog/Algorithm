# 탐색 문제...

from collections import deque

# B연결된 송전탑들의 개수를 세는 함수
def bfs(graph, start, visited):
    queue = deque([start])  # BFS를 위한 큐
    visited[start] = True  # 시작점을 방문 처리
    cnt = 0  # 연결된 송전탑의 개수를 셈
    while queue:
        v = queue.popleft()  # 큐에서 하나의 송전탑을 뽑음
        cnt += 1  # 해당 송전탑을 카운트
        for i in graph[v]:
            if not visited[i]:  # 아직 방문하지 않은 송전탑이면
                queue.append(i)  # 큐에 추가하고 방문 처리
                visited[i] = True
    return cnt  # 연결된 송전탑의 개수를 반환

def solution(n, wires):
    answer = n - 2  # 최대 차이는 n-2, 초기값 설정
    for i in range(len(wires)):  # 모든 전선에 대해 확인
        tmps = wires.copy()  # 원본 wires 배열을 복사
        graph = [[] for i in range(n+1)]  # 송전탑 연결 그래프 초기화
        visited = [False] * (n+1)  # 송전탑 방문 여부 초기화
        tmps.pop(i)  # i번째 전선 제거
        # 전선 정보로 그래프 구성
        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        
        # 첫 번째 송전탑을 찾음 (연결된 송전탑 중 첫 번째)
        for idx, g in enumerate(graph):
            if g != []:  # 연결된 송전탑이 있으면
                start = idx  # 시작점을 설정
                break
        
        # BFS로 첫 번째 전력망에 포함된 송전탑의 개수 구함
        cnts = bfs(graph, start, visited)  
        other_cnts = n - cnts  # 두 번째 전력망의 송전탑 개수는 n - cnts로 구함
        
        # 두 전력망의 송전탑 개수 차이를 계산하고, 최소값을 갱신
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
    
    return answer  # 최소 차이를 반환
