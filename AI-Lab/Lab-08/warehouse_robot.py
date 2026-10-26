warehouse = {
    "Receiving": {"Aisle1": 40, "Aisle2": 70},
    "Aisle1": {"Aisle2": 30, "Packing Station": 90},
    "Aisle2": {"Packing Station": 35},
    "Packing Station": {}
}

heuristic = {
    "Receiving": 100,
    "Aisle1": 70,
    "Aisle2": 35,
    "Packing Station": 0
}


# Calculate actual cost g(n)
def get_g(path):
    total = 0

    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]

        total += warehouse[current_node][next_node]

    return total


# Calculate heuristic h(n)
def get_h(path):
    last_node = path[-1]
    return heuristic[last_node]


# Calculate f(n) = g(n) + h(n)
def get_f(path):
    return get_g(path) + get_h(path)


# A* Search Algorithm
def a_star(start, goal):
    frontier = [[start]]
    explored_count = 0

    while len(frontier) > 0:

        frontier.sort(key=get_f)

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

        if node == goal:
            print("Total nodes explored:", explored_count)
            print("Warehouse search completed successfully.")
            return path

        for neighbour in warehouse[node]:
            new_path = path + [neighbour]
            frontier.append(new_path)

    return None


# Main Program
answer = a_star("Receiving", "Packing Station")

if answer is not None:
    print("\nPath found by A*:", answer)
    print("Total cost:", get_g(answer))
else:
    print("No path found!")
