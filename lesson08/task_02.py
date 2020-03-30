"""2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно
возвращал список вершин, которые необходимо обойти."""
from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    vertex_list = [float('inf')] * length
    path = deque([start])

    cost[start] = 0
    vertex_start = start
    min_cost = 0
    vertex_list[start] = path

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                spam = path.copy()
                spam.append(i)
                vertex_list[i] = spam.copy()
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
                path = vertex_list[i].copy()
    str = ''
    for i in range(length):
        if cost[i] == float('inf'):
            str = str + f'Из вершины {vertex_start} нельзя попасть в вершину {i}.\n'
        else:
            str = str + f'Стоимость пути из вершины {vertex_start} в вершину {i}: {cost[i]}. Кратчайший путь: {list(vertex_list[i])}.\n'
    return str


s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))
