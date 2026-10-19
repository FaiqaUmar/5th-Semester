
maze = {
    "Entrance": ["Hall1", "Hall2"],
    "Hall1": ["Room1"],
    "Hall2": ["Room2", "Trap"],
    "Room1": [],
    "Room2": ["Exit"],
    "Trap": [],
    "Exit": []
}


def dfs_can_reach(maze, start, exit_room):
    visited = []

    def explore(room):
        if room in visited:
            return False

        visited.append(room)

        if room == exit_room:
            return True

        for next_room in maze.get(room, []):
            if explore(next_room):
                return True

        return False

    result = explore(start)
    print("Visit order:", visited)
    return result


reachable = dfs_can_reach(maze, "Entrance", "Exit")
print("Can reach Exit from Entrance?", reachable)
