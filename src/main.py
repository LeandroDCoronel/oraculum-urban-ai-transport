from city_model import generate_circular_city
from slime_optimizer import build_optimized_network
from transport_network import plot_network

def main():
    nodes = generate_circular_city()
    network = build_optimized_network(nodes)
    plot_network(nodes, network)

if __name__ == "__main__":
    main()
