import random
def create_museum_graph(rows=10, cols=10, obstacle_chance=0.1):
    graph = {}
    start_room = 'R0_0'
    all_rooms = [f'R{r}_{c}' for r in range(rows) for c in range(cols) if f'R{r}_{c}' != start_room]
    obstacles = set(random.sample(all_rooms, int(obstacle_chance * len(all_rooms))))

    for r in range(rows):
        for c in range(cols):
            room = f'R{r}_{c}'
            if room in obstacles:
                continue  # Skip creating edges for obstacle rooms

            neighbors = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = r + dr
                new_c = c + dc
                neighbor = f'R{new_r}_{new_c}'
                if 0 <= new_r < rows and 0 <= new_c < cols and neighbor not in obstacles:
                    neighbors.append(neighbor)
            graph[room] = neighbors

    return graph, obstacles
