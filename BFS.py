from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # (room, path)

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None
