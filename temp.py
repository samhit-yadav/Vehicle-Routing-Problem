# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy as np
#import pandas as pd

# Define depot
depot = 0

# Load distance matrix from data
distance_matrix = [
    [0, 48, 49, 44, 51, 43, 31, 40, 35, 26, 21, 25, 39, 34, 27, 32, 22, 15, 60, 56, 45, 35, 22, 20, 17, 21, 15, 11, 23, 25, 22, 18, 21, 13],
    [48, 0, 7, 12, 29, 35, 23, 8, 18, 40, 36, 29, 12, 14, 21, 17, 27, 34, 21, 27, 9, 22, 31, 28, 31, 29, 33, 37, 43, 33, 27, 32, 31, 39],
    [49, 7, 0, 7, 22, 30, 21, 12, 16, 38, 35, 28, 18, 17, 24, 17, 27, 36, 27, 34, 16, 28, 35, 29, 32, 29, 35, 40, 47, 37, 31, 35, 35, 42],
    [44, 12, 7, 0, 18, 24, 15, 12, 10, 31, 28, 21, 19, 14, 22, 12, 22, 33, 33, 38, 19, 28, 32, 24, 27, 23, 30, 35, 45, 35, 27, 31, 32, 38],
    [51, 29, 22, 18, 0, 13, 22, 29, 20, 29, 31, 27, 36, 30, 36, 26, 31, 44, 49, 56, 37, 45, 46, 34, 37, 31, 40, 45, 59, 50, 40, 43, 45, 50],
    [43, 35, 30, 24, 13, 0, 19, 33, 20, 18, 22, 21, 39, 32, 35, 26, 26, 39, 56, 61, 42, 46, 44, 29, 31, 25, 35, 39, 55, 48, 38, 39, 42, 44],
    [31, 23, 21, 15, 22, 19, 0, 18, 5, 17, 13, 6, 22, 15, 16, 8, 9, 22, 42, 44, 26, 28, 25, 12, 15, 9, 18, 23, 38, 29, 19, 21, 24, 28],
    [40, 8, 12, 12, 29, 33, 18, 0, 14, 34, 29, 22, 7, 6, 13, 10, 19, 26, 25, 28, 9, 17, 23, 21, 24, 21, 25, 30, 36, 26, 20, 24, 24, 31],
    [35, 18, 16, 10, 20, 20, 5, 14, 0, 22, 18, 11, 19, 12, 16, 6, 12, 25, 38, 41, 23, 26, 26, 15, 18, 13, 21, 27, 39, 30, 21, 24, 25, 31],
    [26, 40, 38, 31, 29, 18, 17, 34, 22, 0, 7, 12, 38, 30, 29, 24, 17, 27, 59, 60, 43, 41, 33, 19, 19, 16, 22, 25, 43, 38, 28, 28, 32, 31],
    [21, 36, 35, 28, 31, 22, 13, 29, 18, 7, 0, 7, 32, 25, 22, 19, 11, 20, 53, 53, 37, 34, 26, 11, 12, 9, 15, 18, 36, 30, 21, 20, 24, 24],
    [25, 29, 28, 21, 27, 21, 6, 22, 11, 12, 7, 0, 26, 18, 17, 12, 6, 19, 47, 47, 31, 29, 23, 8, 10, 5, 14, 19, 35, 28, 18, 18, 22, 24],
    [39, 12, 18, 19, 36, 39, 22, 7, 19, 38, 32, 26, 0, 8, 12, 14, 21, 24, 22, 22, 6, 10, 20, 22, 24, 23, 24, 28, 31, 21, 17, 22, 20, 29],
    [34, 14, 17, 14, 30, 32, 15, 6, 12, 30, 25, 18, 8, 0, 8, 6, 14, 20, 29, 30, 13, 15, 18, 15, 18, 16, 19, 24, 31, 21, 14, 18, 18, 26],
    [27, 21, 24, 22, 36, 35, 16, 13, 16, 29, 22, 17, 12, 8, 0, 10, 11, 13, 33, 32, 18, 13, 11, 11, 12, 13, 12, 16, 24, 14, 6, 10, 10, 18],
    [32, 17, 17, 12, 26, 26, 8, 10, 6, 24, 19, 12, 14, 6, 10, 0, 10, 20, 35, 36, 19, 20, 21, 12, 15, 12, 18, 23, 34, 24, 15, 19, 20, 26],
    [22, 27, 27, 22, 31, 26, 9, 19, 12, 17, 11, 6, 21, 14, 11, 10, 0, 14, 43, 43, 27, 24, 18, 3, 6, 2, 9, 15, 29, 22, 12, 13, 16, 19],
    [15, 34, 36, 33, 44, 39, 22, 26, 25, 27, 20, 19, 24, 20, 13, 20, 14, 0, 45, 40, 30, 20, 8, 11, 8, 14, 5, 4, 16, 12, 7, 2, 6, 6],
    [60, 21, 27, 33, 49, 56, 42, 25, 38, 59, 53, 47, 22, 29, 33, 35, 43, 45, 0, 12, 16, 25, 39, 44, 46, 45, 46, 49, 47, 38, 38, 42, 40, 48],
    [56, 27, 34, 38, 56, 61, 44, 28, 41, 60, 53, 47, 22, 30, 32, 36, 43, 40, 12, 0, 19, 20, 33, 42, 44, 45, 43, 45, 39, 31, 35, 38, 35, 43],
    [45, 9, 16, 19, 37, 42, 26, 9, 23, 43, 37, 31, 6, 13, 18, 19, 27, 30, 16, 19, 0, 15, 26, 28, 30, 29, 31, 35, 37, 26, 24, 28, 26, 35],
    [35, 22, 28, 28, 45, 46, 28, 17, 26, 41, 34, 29, 10, 15, 13, 20, 24, 20, 25, 20, 15, 0, 13, 23, 24, 26, 23, 25, 22, 13, 14, 18, 15, 23],
    [22, 31, 35, 32, 46, 44, 25, 23, 26, 33, 26, 23, 20, 18, 11, 21, 18, 8, 39, 33, 26, 13, 0, 15, 14, 19, 12, 12, 13, 4, 6, 6, 2, 10],
    [20, 28, 29, 24, 34, 29, 12, 21, 15, 19, 11, 8, 22, 15, 11, 12, 3, 11, 44, 42, 28, 23, 15, 0, 3, 3, 6, 12, 27, 20, 10, 10, 14, 16],
    [17, 31, 32, 27, 37, 31, 15, 24, 18, 19, 12, 10, 24, 18, 12, 15, 6, 8, 46, 44, 30, 24, 14, 3, 0, 6, 4, 9, 24, 19, 10, 8, 12, 13],
    [21, 29, 29, 23, 31, 25, 9, 21, 13, 16, 9, 5, 23, 16, 13, 12, 2, 14, 45, 45, 29, 26, 19, 3, 6, 0, 9, 14, 30, 23, 13, 14, 17, 19],
    [15, 33, 35, 30, 40, 35, 18, 25, 21, 22, 15, 14, 24, 19, 12, 18, 9, 5, 46, 43, 31, 23, 12, 6, 4, 9, 0, 5, 21, 16, 8, 6, 10, 10],
    [11, 37, 40, 35, 45, 39, 23, 30, 27, 25, 18, 19, 28, 24, 16, 23, 15, 4, 49, 45, 35, 25, 12, 12, 9, 14, 5, 0, 18, 15, 11, 7, 10, 6],
    [23, 43, 47, 45, 59, 55, 38, 36, 39, 43, 36, 35, 31, 31, 24, 34, 29, 16, 47, 39, 37, 22, 13, 27, 24, 30, 21, 18, 0, 10, 18, 16, 14, 12],
    [25, 33, 37, 35, 50, 48, 29, 26, 30, 38, 30, 28, 21, 21, 14, 24, 22, 12, 38, 31, 26, 13, 4, 20, 19, 23, 16, 15, 10, 0, 10, 10, 6, 12],
    [22, 27, 31, 27, 40, 38, 19, 20, 21, 28, 21, 18, 17, 14, 6, 15, 12, 7, 38, 35, 24, 14, 6, 10, 10, 13, 8, 11, 18, 10, 0, 4, 5, 12],
    [18, 32, 35, 31, 43, 39, 21, 24, 24, 28, 20, 18, 22, 18, 10, 19, 13, 2, 42, 38, 28, 18, 6, 10, 8, 14, 6, 7, 16, 10, 4, 0, 4, 8],
    [21, 31, 35, 32, 45, 42, 24, 24, 25, 32, 24, 22, 20, 18, 10, 20, 16, 6, 40, 35, 26, 15, 2, 14, 12, 17, 10, 10, 14, 6, 5, 4, 0, 8],
    [13, 39, 42, 38, 50, 44, 28, 31, 31, 31, 24, 24, 29, 26, 18, 26, 19, 6, 48, 43, 35, 23, 10, 16, 13, 19, 10, 6, 12, 12, 12, 8, 8, 0]
]

# Define milk volumes at each pickup point
milk_volumes = {
    1: 310,  # Pickup point 1: Khandibara, Thadgam, Aathadungari
    2: 540,  # Pickup point 2: Jamba, Nalwant, Vadhay
    3: 1280, # Pickup point 3: Sandhaliya, Palasani, Kandwa, Kukawati
    4: 350,  # Pickup point 4: Nawagam, Vanthada, Pochamba
    5: 210,  # Pickup point 5: Kandha, Baroli
    6: 405,  # Pickup point 6: Nannupura, Haripura, Sindhikuwa
    7: 880,  # Pickup point 7
    8: 260,  # Pickup point 8
    9: 220,  # Pickup point 9
    10: 230, # Pickup point 10
    11: 560, # Pickup point 11
    12: 690, # Pickup point 12
    13: 820, # Pickup point 13
    14: 950, # Pickup point 14
    15: 570, # Pickup point 15
    16: 690, # Pickup point 16
    17: 210, # Pickup point 17
    18: 130, # Pickup point 18
    19: 240, # Pickup point 19
    20: 890, # Pickup point 20
    21: 290, # Pickup point 21
    22: 800, # Pickup point 22
    23: 610, # Pickup point 23
    24: 300, # Pickup point 24
    25: 100, # Pickup point 25
    26: 770, # Pickup point 26
    27: 930, # Pickup point 27
    28: 220, # Pickup point 28
    29: 140, # Pickup point 29
    30: 370, # Pickup point 30
    31: 100, # Pickup point 31
    32: 360, # Pickup point 32
    33: 230  # Pickup point 33
}

# Number of societies represented by each pickup point (for waiting time calculation)
societies_per_point = {
    1: 3, 2: 3, 3: 4, 4: 3, 5: 2, 6: 3,
    7: 3, 8: 2, 9: 2, 10: 2, 11: 2,
    12: 2, 13: 3, 14: 3, 15: 2, 16: 3, 17: 2,
    18: 3, 19: 2, 20: 4, 21: 3, 22: 4,
    23: 2, 24: 2, 25: 2, 26: 2, 27: 3,
    28: 2, 29: 2, 30: 3, 31: 2, 32: 2, 33: 2
}

# Vehicle capacity in liters
vehicle_capacity = 4000

# Average speed in km/hr
average_speed = 30

# Max time allowed for route (in hours)
max_route_time = 7

# Waiting time per society (in minutes)
waiting_time_per_society = 5

# Calculate savings for all possible pairs
savings = {}
for i in range(1, 34):  # Pickup points 1 to 33
    for j in range(i+1, 34):  # Avoid duplicates
        savings[(i, j)] = distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]

# Sort savings in descending order
sorted_savings = sorted(savings.items(), key=lambda x: x[1], reverse=True)

# Initialize routes - start with direct routes from depot to each pickup point
routes = [[i] for i in range(1, 34)]

# Map to track which route each node belongs to
node_to_route = {}
for i in range(1,34):
    node_to_route[i] = i-1

# Function to calculate route distance
def calculate_route_distance(route, distance_matrix):
    
    #Calculate the total distance for a given route.
    
    if not route:  # Handle empty route case
        return 0

    # Distance  depot -> first node
    total_distance = distance_matrix[depot][route[0]]

    # Distance between consecutive nodes in the route
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]

    # Distance  last node -> depot
    total_distance += distance_matrix[route[-1]][depot]

    return total_distance





# Function to calculate route time
def calculate_route_time(route, distance_matrix, average_speed, societies_per_point, waiting_time_per_society):
    distance = calculate_route_distance(route,distance_matrix)
    
    # Calculate travel time in hours
    travel_time = distance / average_speed
    
    # Calculate waiting time in hours
    waiting_time = sum(societies_per_point[node] * waiting_time_per_society for node in route) / 60
    
    # Total route time
    return travel_time + waiting_time



# function to get milk route volume
def get_route_milk_volume(route):
    total_milk_volume = 0

    for node in route:
        node_milk_volume = milk_volumes[node]
        total_milk_volume = total_milk_volume + node_milk_volume
    
    return total_milk_volume



# Merge routes based on savings
for (i, j), saving in sorted_savings:
    route_i = node_to_route[i]
    route_j = node_to_route[j]
    
    # Skip if nodes are already in the same route
    if route_i == route_j:
        continue
    
    route_i_nodes = routes[route_i]
    route_j_nodes = routes[route_j]
    
    # Check if nodes are at ends of their routes
    i_at_start = route_i_nodes[0] == i
    i_at_end = route_i_nodes[-1] == i
    j_at_start = route_j_nodes[0] == j
    j_at_end = route_j_nodes[-1] == j
    
    # Both nodes must be connected to depot
    if not ((i_at_start or i_at_end) and (j_at_start or j_at_end)):
        continue
    
    # Determine how to merge the routes
    if i_at_end and j_at_start:
        new_route = route_i_nodes + route_j_nodes
    elif i_at_start and j_at_end:
        new_route = route_j_nodes + route_i_nodes
    elif i_at_end and j_at_end:
        new_route = route_i_nodes + list(reversed(route_j_nodes))
    elif i_at_start and j_at_start:
        new_route = list(reversed(route_i_nodes)) + route_j_nodes
    else:
        continue  
    
    # Check capacity constraint
    if get_route_milk_volume(new_route) > vehicle_capacity:
        continue
    
    # Check time constraint
    if calculate_route_time(new_route, distance_matrix, average_speed, societies_per_point, waiting_time_per_society) > max_route_time:
        continue
    
    # Merge is valid - update routes
    routes[route_i] = new_route
    routes[route_j] = []  # Empty the other route
    
    # Update node-to-route mappings
    for node in new_route:
        node_to_route[node] = route_i

# Remove empty routes
routes = [r for r in routes if r]



# list of route_details objects
final_routes = []
for route in routes:
    # route_details is an object
    route_details = {
        'route': [0] + route + [0],  # Ensure route is a list before adding
        'milk_volume': get_route_milk_volume(route),
        'time': calculate_route_time(route, distance_matrix, average_speed, societies_per_point, waiting_time_per_society),
        'distance': calculate_route_distance(route, distance_matrix)
    }
    final_routes.append(route_details)


# Display results
print("Optimized Routes:")
for i, route in enumerate(final_routes):
    print(f"\nRoute {i+1}:")
    path = " → ".join(str(node) for node in route['route'])
    print(f"Path: {path}")
    print(f"Milk Volume: {route['milk_volume']} liters")
    print(f"Route Time: {route['time']:.2f} hours")
    print(f"Route Distance: {route['distance']} km")

# Calculate and display savings
original_distance = sum(distance_matrix[0][i] * 2 for i in range(1, 34))
optimized_distance = sum(route['distance'] for route in final_routes)
distance_savings = original_distance - optimized_distance
percent_savings = (distance_savings / original_distance) * 100

print("\nSummary:")
print(f"Total Original Distance (individual routes): {original_distance} km")
print(f"Total Optimized Distance: {optimized_distance} km")
print(f"Distance Savings: {distance_savings} km ({percent_savings:.2f}%)")
print(f"Number of Routes: {len(final_routes)}")







