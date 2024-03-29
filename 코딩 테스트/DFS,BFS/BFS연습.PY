# from collections import deque
# def BFS(graph, start, visited):
#     visited[start] = True
#     queue = deque([start])
    
#     while queue:
#         v = queue.popleft()
#         print(v, end='')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
# from collections import deque
# def BFS(graph, start, visited):
#     visited[start] = True
#     queue =  deque([start])
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True                
from collections import deque
def BFS(graph, start, visted):
    visited[start] = True
    queue = deque([start])
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

BFS(graph,1,visited)