# Weighted Graph
graph = {
    "S": {"A": 6, "B": 5, "C": 10},
    "A": {"E": 6},
    "B": {"E": 6, "D": 7},
    "C": {"D": 6},
    "D": {"F": 6},
    "E": {"F": 4},
    "F": {"G": 3},
    "G": {}
}

# Heuristic values
heuristic = {
    "S": 17,
    "A": 10,
    "B": 13,
    "C": 4,
    "D": 2,
    "E": 4,
    "F": 1,
    "G": 0
}


# Calculate actual path cost: g(n)
def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]

        total = total + graph[current_node][next_node]

    return total


# Calculate heuristic value: h(n)
def get_h(path):
    last_node = path[-1]
    return heuristic[last_node]


# Calculate evaluation function: f(n) = g(n) + h(n)
def get_f(path):
    return get_g(path) + get_h(path)


# A* Search Algorithm
def a_star(start, goal):

    frontier = [[start]]
    explored_count = 0

    while len(frontier) > 0:

        # Sort frontier based on f(n)
        frontier.sort(key=get_f)

        # Select path with lowest f(n)
        path = frontier.pop(0)
        node = path[-1]

        explored_count += 1

        print(
            "Exploring:", node,
            "| Path:", path,
            "| g =", get_g(path),
            "| h =", get_h(path),
            "| f =", get_f(path)
        )

        # Check goal
        if node == goal:
            print("\nTotal nodes explored:", explored_count)
            return path

        # Expand neighbours
        for neighbour in graph[node]:
            new_path = path + [neighbour]
            frontier.append(new_path)

    print("\nTotal nodes explored:", explored_count)
    return None


# Main Program
answer = a_star("S", "G")

if answer is not None:
    print("\nPath found by A*:", answer)
    print("Total cost of this path:", get_g(answer))
else:
    print("No path found!")
