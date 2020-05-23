def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def fast_pow(a: float, n: int):
    if n == 0:
        return 1
    elif (n % 2) == 1:
        fast_pow(a, n - 1) * n
    else:
        fast_pow(a ** 2, n // 2)


def permutation(n, m, prefix=None):
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for i in range(n):
        if i in prefix:
            continue
        prefix.append(i)
        permutation_with_repetition(n, m - 1, prefix)
        prefix.pop()


def permutation_with_repetition(n, m, prefix=None):
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for i in range(n):
        prefix.append(i)
        permutation_with_repetition(n, m - 1, prefix)
        prefix.pop()


import graph
import queue

graph = graph.Graph()
for i in range(5):
    graph.addVertex(i)
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 5)
graph.addEdge(2, 3)
graph.addEdge(2, 4)

for v in graph:
    for nbr in v.getConnections():
        pass

path = list()


def bfs(start, graph):
    start.setColor('Gray')
    distances = dict()
    distances[start] = 0
    vertQueue = queue.Queue()
    vertQueue.push(start)

    while vertQueue.size() > 0:
        currentVert = vertQueue.pop()
        for neighbor in currentVert.getConnections():
            if neighbor.getColor() == 'White':
                neighbor.setColor('Gray')
                distances[neighbor] = distances[currentVert] + 1
                vertQueue.push(neighbor)
                path.append(neighbor.getId())
                print(path)
        currentVert.setColor('Black')


bfs(graph.vertexList[0], graph)
print(path)
