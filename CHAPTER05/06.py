"""
그래프를 어떻게 표현하는지는 확인했으니

본격적으로 DFS이다.
기본 이론은 다음과 같다.

0. 스택을 사용한다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고
방문 처리를 한다.
방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다. 
3. 2번의 과정을 계속 반복하여 모두 방문하도록 한다.


위를 재귀적으로 해석해보자.

기본이론은 내가 현재 있는 노드 기준으로 주위에 방문하지 않은 노드를 찾아서
그쪽에서 다시 똑같은 함수를 실행한다.
"""


def dfs(graph, v, visited):
    visited[v] = True  # 자기자신은 방문했다고 작성하고
    print(v, end=' ')  # 방문했으니깐 출력
    for i in graph[v]:  # v와 인접한 노드 모두를 체크하는데
        if not visited[i]:  # 만약 방문하지 않았다면
            dfs(graph, i, visited)  # 그 방문하지 않은 노드에 대해서 dfs를 다시 실행


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9

dfs(graph, 1, visited)