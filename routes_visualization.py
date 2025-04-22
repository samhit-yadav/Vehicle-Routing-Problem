

import networkx as nx
import matplotlib.pyplot as plt

# Define optimized routes
optimized_routes = {
    1: [0, 25, 3, 2, 1, 20, 18, 19, 21, 0],
    2: [0, 24, 23, 16, 11, 6, 8, 4, 5, 9, 10, 0],
    3: [0, 15, 13, 7, 12, 14, 0],
    4: [0, 26, 17, 31, 30, 32, 22, 29, 28, 33, 0],
    5: [0, 27, 0]
}

# Colors for each route
route_colors = ['red', 'blue', 'green', 'magenta', 'cyan']
G = nx.DiGraph()
edge_colors = []
node_colors = {}
labels_for_legend = {}

# Add edges and color nodes by route
for route_id, path in optimized_routes.items():
    color = route_colors[route_id - 1]
    labels_for_legend[color] = f'Route {route_id}'
    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1], color=color)
        edge_colors.append(color)
        # Assign color to each node (except depot 0 which will be colored later)
        if path[i] != 0:
            node_colors[path[i]] = color
        if path[i+1] != 0:
            node_colors[path[i+1]] = color

# Color depot (0) with a distinct color
node_colors[0] = 'orange'  # Depot node

# Prepare node color list for drawing
node_color_list = [node_colors.get(node, 'gray') for node in G.nodes()]
edge_color_list = [G[u][v]['color'] for u, v in G.edges()]

# Draw graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, node_color=node_color_list, edge_color=edge_color_list, with_labels=True, node_size=600, width=2)

# Create custom legend
from matplotlib.patches import Patch
legend_handles = [Patch(color=color, label=label) for color, label in labels_for_legend.items()]
legend_handles.append(Patch(color='orange', label='Depot (0)'))

plt.legend(handles=legend_handles, loc='upper left', bbox_to_anchor=(1, 1))
plt.title("Optimized Milk Collection Routes")
plt.tight_layout()
plt.show()
