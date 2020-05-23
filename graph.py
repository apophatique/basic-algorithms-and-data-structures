# python 3.5.2
class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = dict()

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def getId(self):
        return self.id


class AdvancedVertex(Vertex):
    def __init__(self, key):
        super().__init__(key)
        self.color = None
        self.pred = None

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPred(self, pred):
        self.pred = pred

    def getPred(self):
        return self.pred


class Graph:
    def __init__(self):
        self.vertList = dict()

    def addVertex(self, key):
        newVert = AdvancedVertex(key)
        self.vertList[key] = newVert
        return self.vertList[key]

    def __contains__(self, vert):
        return vert in self.vertList

    def getVertex(self, key):
        return self.vertList[key] if key in self.vertList else None

    def addConnection(self, init, final, weight=0):
        if init not in self.vertList:
            self.addVertex(init)
        if final not in self.vertList:
            self.addVertex(final)
        self.vertList[init].addNeighbor(self.vertList[final], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


class GraphBDFS(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self, graph):
        for vert in graph:
            vert.setColor('White')

        for nbr in graph:
            if nbr.getColor() == 'White':
                self.dfsStep(nbr)

    def dfsStep(self, startVertex):
        startVertex.setColor('Gray')
        print('This: ', startVertex.getId())
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'White':
                nextVertex.setPred(startVertex)
                self.dfsStep(nextVertex)
        startVertex.setColor('Black')

    def bfs(self, graph, start):
        vertQueue = Queue()
        path = list()

        for vert in graph:
            vert.setColor('White')
        start.setColor('Gray')
        vertQueue.push(start)
        path.append(start)
        while (vertQueue.size() > 0):
            currentVert = vertQueue.pop()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'White'):
                    nbr.setColor('Gray')
                    nbr.setPred(currentVert)
                    path.append(nbr)
                    vertQueue.push(nbr)
            currentVert.setColor('Black')
        return path


if __name__ == "__main__":
    graph = Graph()
    graphSearch = GraphBDFS()

    for i in range(6):
        graph.addVertex(i)
    graph.addConnection(0, 1)
    graph.addConnection(0, 3)
    graph.addConnection(0, 5)
    graph.addConnection(0, 7)
    graph.addConnection(1, 2)
    graph.addConnection(1, 4)
    graph.addConnection(1, 6)
    graph.addConnection(2, 8)
    graph.addConnection(1, 9)
    graph.addConnection(9, 1)
    for vert in graph:
        for nbr in vert.getConnections():
            print("{parent}: {neighbor}".format(parent=vert.getId(),
                                                neighbor=nbr.getId()))

    bfsVertList = graphSearch.bfs(graph, graph.getVertex(0))
    graphSearch.dfs(graph)
    print('DFS result: \n', [vertex.getId() for vertex in bfsVertList])
