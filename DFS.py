def dfs(graph, current, visited, alarm_triggered_func):
    visited.append(current)
    print(f"Patrolling: {current}")

    if alarm_triggered_func():
        print(f"Alarm triggered during DFS at: {current}")
        return visited, current  # Stop DFS here

    for neighbor in graph[current]:
        if neighbor not in visited:
            path, stop_room = dfs(graph, neighbor, visited, alarm_triggered_func)
            if stop_room:  # alarm triggered in deeper call
                return path, stop_room

    return visited, None
