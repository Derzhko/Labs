from Dijkstra.PriorityQueue import PriorityQueue
import sys
import time
from random import random, seed
from random import randint, choice

class Dijkstra:
    def run(self, n, m):
        startVertex, endVertex = 1, n
        startVertex -= 1
        endVertex -= 1
        graph = [[] for i in range(n)]
        def getWeight():
            return randint(1, 10**6)
        def getVertex():
            return randint(1, n)
        for i in range(m):
            start, end, weight = getVertex(), getVertex(), getWeight()
            start -= 1
            end -= 1
            graph[start].append((end, weight))
        d = [sys.maxsize for i in range(n)]
        d[startVertex] = 0
        q = PriorityQueue()
        q.push((0, startVertex))
        while not q.isEmpty():
            curD, v = q.pop()
            if (curD > d[v]): continue
            for j in range(len(graph[v])):
                to = graph[v][j][0]
                weight = graph[v][j][1]
                if d[v] + weight < d[to]:
                    d[to] = d[v] + weight
                    q.push((-d[to], to))
        return d[endVertex]

class DijkstraMeasure:
    __dijkstra = Dijkstra()
    def __init__(self) -> None:
        seed(228)

    def measure(self, n, m):
        timeStart= time.time()
        self.__dijkstra.run(n, m)
        timeEnd = time.time()
        return timeEnd - timeStart

    def __generateTest(self, n, m):
        def getWeight():
            return randint(1, 10**6)
        def getVertex():
            return randint(1, n)
        def getUniqPair():
            first = getVertex()
            second = getVertex()
            while first == second:
                second = getVertex()
            return first, second
        test = f"{n} {m}\n"
        test += f"{1} {n}\n"
        for _ in range(m):
            start, end = getUniqPair()
            test += f"{start} {end} {getWeight()}\n"
        with open("inputDijkstra.txt", 'w') as inputFile:
            inputFile.write(test)
