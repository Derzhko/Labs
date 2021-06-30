#  тут Беллман

import sys
import time
from random import seed
from random import randint

class Edge:
    a = 0
    b = 0
    weight = 0
    def __init__(self, a, b, w) -> None:
        self.a = a
        self.b = b
        self.weight = w

class BellmanFord:
    def run(self, n, m):
        def getWeight():
            return randint(1, 10**6)
        def getVertex():
            return randint(1, n)
        e = []
        d = [sys.maxsize for i in range(n)]
        for i in range(m):
            start, end, weight =getVertex(), getVertex(), getWeight()
            start -= 1
            end -= 1
            e.append(Edge(start, end, weight))
        while True:
            any = False
            for j in range(m):
                if d[e[j].a] < sys.maxsize:
                    if d[e[j].b] > d[e[j].a] + e[j].weight:
                        d[e[j].b] = d[e[j].a] + e[j].cost
                        any = True
            if not any: break

class BellmanFordMeasure:
    __bellmanFord = BellmanFord()
    def __init__(self) -> None:
        seed(228)

    def measure(self, n, m):
        timeStart= time.time()
        self.__bellmanFord.run(n, m)
        timeEnd = time.time()
        return timeEnd - timeStart

    def __generateTest(self, n, m):
        test = f"{n} {m} {1}\n"
        vertexs = [vertex for vertex in range(n)]
        def getWeight():
            return randint(1, 10**6)
        def getVertex():
            return randint(1, n)
        for _ in range(m):
            test += f"{getVertex()} {getVertex()} {getWeight()}\n"
        with open("inputBellmanFord.txt", 'w') as inputFile:
            inputFile.write(test)
