import numpy as np

def generate_circular_city(num_rings=3, nodes_per_ring=12):
    nodes = []

    for r in range(1, num_rings + 1):
        radius = r * 10
        for i in range(nodes_per_ring):
            angle = 2 * np.pi * i / nodes_per_ring
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            nodes.append((x, y))

    return np.array(nodes)
