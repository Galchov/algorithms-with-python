"""
Input:
8
A - B - 2
A - C - 4
B - C - 1
B - D - 4
C - D - 3
C - E - 5
D - E - 2
B - E - 1
B-D
A
E
Output:
A - B - E
3
"""


def dijkstra(graph, start, end):
    distances = {city: float("inf") for city in graph}
    distances[start] = 0
    previous_nodes = {city: None for city in graph}
    unvisited = set(graph.keys())

    while unvisited:
        current_city = min(unvisited, key=lambda city: distances[city])
        unvisited.remove(current_city)

        if distances[current_city] == float("inf"):
            break

        for neighbor, distance in graph.get(current_city, []):
            new_distance = distances[current_city] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_city

        if current_city == end:
            break

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous_nodes[current]

    return path if path[0] == start else None, distances[end]


r = int(input())
roads = []
for _ in range(r):
    road = input()
    city1, city2, distance = road.split(" - ")
    distance = int(distance)
    roads.append((city1, city2, distance))

closed_roads_input = input()
closed_roads = set(tuple(sorted(road.split("-"))) for road in closed_roads_input.split(","))

start_city = input()
end_city = input()

graph = {}
for city1, city2, distance in roads:
    if tuple(sorted([city1, city2])) not in closed_roads:
        graph.setdefault(city1, []).append((city2, distance))
        graph.setdefault(city2, []).append((city1, distance))

shortest_path, total_distance = dijkstra(graph, start_city, end_city)

if shortest_path:
    print(" - ".join(shortest_path))
    print(total_distance)
else:
    print("No path found")
