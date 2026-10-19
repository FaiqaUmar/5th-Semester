
from collections import deque

network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara"]
}


def bfs_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return None

    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        person = path[-1]

        if person == goal:
            return path

        for friend in graph[person]:
            if friend not in visited:
                visited.add(friend)
                queue.append(path + [friend])

    return None


start = "Ali"
goal = "Hira"

path = bfs_shortest_path(network, start, goal)

if path:
    print(f"Shortest chain from {start} to {goal}: {path}")
    print(f"Number of introductions needed: {len(path) - 1}")
else:
    print(f"No connection found between {start} and {goal}.")
