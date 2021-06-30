import matplotlib.pyplot as plt

def plot(fileName):
    file = open(f"{fileName}.txt", 'r')
    nums = list(map(float, file.read()[:-1].split()))
    x = [xi for xi in range(10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)]
    y = nums

    plt.plot(x,y)
    plt.xlabel('Number of vertices')
    plt.ylabel('Time')
    plt.title(f'{fileName}', fontsize=16, fontname='Arial')
    plt.savefig(f"{fileName}.png")
    plt.show()
    plt.clf()

def plotDijkstraOne():
    file = open(f"dijkstraOne.txt", 'r')
    nums = list(map(float, file.read()[:-1].split()))
    x = [xi for xi in range(10 ** 3, 10 ** 3 + 1000 * len(nums), 1000)]
    y = nums

    plt.plot(x, y)
    plt.xlabel('Number of vertices')
    plt.ylabel('Time')
    plt.title('Dijkstra a', fontsize=16, fontname='Arial')
    plt.savefig(f"dijkstraOne.png")
    plt.show()
    plt.clf()

# dijkstraA >> 10 ** 3, 10 ** 3 + 1000 * len(nums), 1000)
# dijkstraB >> 10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)
# bellmanFordA >>  10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)
# bellmanFordB >> 10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)

plotDijkstraOne()
plot('dijkstraTwo')
plot('bellmanFordOne')
plot('bellmanFordTwo')
