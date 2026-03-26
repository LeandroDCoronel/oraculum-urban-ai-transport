import matplotlib.pyplot as plt

def plot_network(nodes, graph):
    for edge in graph.edges():
        x = [nodes[edge[0]][0], nodes[edge[1]][0]]
        y = [nodes[edge[0]][1], nodes[edge[1]][1]]
        plt.plot(x, y, 'k-', alpha=0.5)

    plt.scatter(nodes[:,0], nodes[:,1], c='red')
    plt.title("AI-Optimized Transport Network (Slime Inspired)")
    plt.show()
