import pygame
import random
from DFS import dfs
from BFS import bfs
from metrics import show_metrics
from map import create_museum_graph
from visual import draw_grid, animate_path

alarm_chance_per_room = 0.1  # 10% chance per room visit

def main():
    #Paygame setup
    pygame.init()
    screen = pygame.display.set_mode((470,470))
    pygame.display.set_caption("Museum Guard Patrol")

    # Create graph
    graph, obstacles = create_museum_graph(rows=10, cols=10)
    visited_DFS = []
    start_room = 'R0_0'

    # Alarm trigger
    possible_alarm_rooms = [room for room in graph.keys() if room not in obstacles]
    alarm_room = random.choice(possible_alarm_rooms) # The room where the alarm triggered
    alarm_triggered = False
    def alarm_triggered_func():
        nonlocal alarm_triggered
        if not alarm_triggered and random.random() < alarm_chance_per_room:
            alarm_triggered = True
        return alarm_triggered

    # Perform DFS until alarm triggers
    patrol_path, stopped_room = dfs(graph, start_room, visited_DFS, alarm_triggered_func)

    # Animate DFS part
    draw_grid(screen, visited_DFS, alarm=alarm_room, obstacles=obstacles)
    animate_path(screen, patrol_path, visited_DFS, obstacles=obstacles)

    # BFS response
    # Enabling the guard to reach the disturbance point as fast as possible
    bfs_path = None
    if alarm_triggered:
        print(f"\nAlarm triggered in room: {alarm_room}")
        bfs_path = bfs(graph, stopped_room, alarm_room)
        draw_grid(screen, visited_DFS, alarm=alarm_room, bfs_path=bfs_path, obstacles=obstacles)
        animate_path(screen, bfs_path, visited_DFS, alarm=alarm_room, bfs_path=bfs_path,obstacles=obstacles)

    show_metrics(patrol_path, bfs_path)

    print("Press any key or close the window to exit.")
    while True:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.KEYDOWN]:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
