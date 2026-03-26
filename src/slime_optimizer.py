from scipy.spatial import distance_matrix
import networkx as nx

def build_optimized_network(nodes):
    dist_matrix = distance_matrix(nodes, nodes)

    G = nx.Graph()

    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            G.add_edge(i, j, weight=dist_matrix[i][j])

    mst = nx.minimum_spanning_tree(G)
    return mst