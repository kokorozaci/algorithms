"""1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа."""

n = int(input("Введите число друзей: "))


def flattenedges(graph):
    if len(graph) == 1:
        return graph[0]
    else:
        return graph[0] + flattenedges(graph[1:])


def graph(nodes):
    edges = []

    for i in range(nodes):
        edges.append([])
        for j in range(nodes):
            if i > j:
                edges[i].append(1)
            else:
                edges[i].append(0)

    return edges


print(*graph(n), sep='\n')
print(f'Всего рукопожатий было: {sum(flattenedges(graph(n)))}')
