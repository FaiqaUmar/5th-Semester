
import heapq
from itertools import count

flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": []
}


def ucs_cheapest_route(graph, start, goal):
    explored_count = 0
    sequence = count()

    queue = [(0, next(sequence), [start])]
    visited = set()

    while queue:
        cost, _, route = heapq.heappop(queue)

        explored_count += 1

        city = route[-1]

        print(f"Exploring: {route} | Cost: {cost}")

        if city in visited:
            continue

        visited.add(city)

        if city == goal:
            return route, cost, explored_count

        for next_city, ticket_price in graph.get(city, []):
            if next_city not in visited:
                heapq.heappush(
                    queue,
                    (
                        cost + ticket_price,
                        next(sequence),
                        route + [next_city]
                    )
                )

    return None, None, explored_count


route, total_cost, explored_count = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)

if route:
    print("Cheapest route:", route)
    print("Total ticket cost:", total_cost)
else:
    print("No route found.")

print("Total routes explored:", explored_count)
