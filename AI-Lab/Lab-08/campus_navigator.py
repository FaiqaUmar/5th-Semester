campus = {
    "Hostel": {
        "Cafeteria": 150,
        "Admin Block": 300,
        "Sports Complex": 180
    },
    "Cafeteria": {"Academic Block": 200},
    "Admin Block": {"Academic Block": 120},
    "Sports Complex": {"Academic Block": 250},
    "Academic Block": {"Library": 100},
    "Library": {}
}

heuristic = {
    "Hostel": 350,
    "Cafeteria": 260,
    "Admin Block": 150,
    "Sports Complex": 240,
    "Academic Block": 90,
    "Library": 0
}

def get_h(path):
    last_node = path[-1]
    return heuristic[last_node]


def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        total += campus[current_node][next_node]

    return total


def gbfs(start, goal):
    frontier = [[start]]
    visited = []
    explored_count = 0

    while len(frontier) > 0:
        frontier.sort(key=get_h)

        path = frontier.pop(0)
        node = path[-1]

        if node in visited:
            continue

        visited.append(node)
        explored_count += 1

        print(
            "Exploring:", node,
            "| Path:", path,
            "| h =", get_h(path)
        )

        if node == goal:
            print("Total nodes explored:", explored_count)
            return path

        for neighbour in campus[node]:
            new_path = path + [neighbour]
            frontier.append(new_path)

    return None


answer = gbfs("Hostel", "Library")

if answer is not None:
    print("\nPath found by GBFS:", answer)
    print("Total cost of this path:", get_g(answer))
else:
    print("No path found!")
