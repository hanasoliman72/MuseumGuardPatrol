TOTAL_ROOMS = 100

def show_metrics(patrol_path, bfs_path):
    print("\n--- METRICS ---")
    print(f"DFS Patrol Order: {patrol_path}")
    print(f"Total Rooms Patrolled (DFS): {len(patrol_path)}")

    if bfs_path:
        print(f"Alarm Response Path (BFS): {bfs_path}")
        print(f"Response Time (steps): {len(bfs_path) - 1}")
    else:
        print("No alarm triggered or response path not found.")

    visited_rooms = set(list(patrol_path) + list(bfs_path))
    coverage_percent = (len(visited_rooms) / TOTAL_ROOMS) * 100
    print(f"Coverage: {coverage_percent:.2f}%")
