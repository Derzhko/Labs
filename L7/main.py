from Bellman.BellmanFord import BellmanFordMeasure
from Dijkstra.Dijkstra import DijkstraMeasure

def saveTimesWithName(times, name):
    toSave = " "
    for time in times:
        toSave += f"{time} "
    file = open(f"{name}.txt", 'a')
    file.write(toSave)
    file.close()

def collectDataDijkstraA():
    dijkstra = DijkstraMeasure()
    dijkstraTimes = []
    n = 10 ** 4
    for m in range(10 ** 5, 10 ** 7, 10 ** 5):
        print(m / 10 ** 7 * 100)
        timedijkstra = dijkstra.measure(n=n, m=m)
        saveTimesWithName([timedijkstra], "dijkstraOne")
        dijkstraTimes.append(timedijkstra)

def collectDataDijkstraB():
    dijkstra = DijkstraMeasure()
    n = 10 ** 4
    for m in range(10 ** 3, 10 ** 5, 10 ** 3):
        print(m / 10 ** 5 * 100)
        timedijkstra = dijkstra.measure(n=n, m=m)
        saveTimesWithName([timedijkstra], "dijkstraTwo")

def collectDataBellmanFordA():
    bellmanFord = BellmanFordMeasure()
    n = 10 ** 4
    for m in range(10 ** 5, 10 ** 7, 10 ** 5):
        print(m / 10 ** 7 * 100)
        timeBellman = bellmanFord.measure(n=n, m=m)
        saveTimesWithName([timeBellman], "bellmanFordOne")

def collectDataBellmanFordB():
    bellmanFord = BellmanFordMeasure()
    n = 10 ** 4
    for m in range(10 ** 3, 10 ** 5, 10 ** 3):
        print(m / 10 ** 5 * 100)
        timeBellman = bellmanFord.measure(n=n, m=m)
        saveTimesWithName([timeBellman], "bellmanFordTwo")

collectDataDijkstraA()
collectDataDijkstraB()
collectDataBellmanFordA()
collectDataBellmanFordB()
exit()
