import pygame
import time

ROOM_SIZE = 40
MARGIN = 6
ROWS, COLS = 10, 10
FPS = 3  # Steps per second

# Soft Color Palette
BACKGROUND_COLOR = (240, 248, 255)      # AliceBlue
GRID_LINE_COLOR = (200, 200, 200)       # Light Gray
ROOM_COLOR = (255, 255, 255)            # White
VISITED_COLOR = (200, 220, 240)         # Light Blue Gray
GUARD_COLOR = (100, 149, 237)           # Cornflower Blue
ALARM_COLOR = (255, 99, 71)             # Tomato
BFS_COLOR = (255, 215, 0)               # Gold
OBSTACLE_COLOR = (169, 169, 169)        # Dark Gray

def get_room_position(room_id):
    r, c = map(int, room_id[1:].split('_'))
    return c, r  # x, y

def draw_grid(screen, visited, current=None, alarm=None, bfs_path=None, obstacles=None):
    screen.fill(BACKGROUND_COLOR)
    if obstacles is None:
        obstacles = set()

    for r in range(ROWS):
        for c in range(COLS):
            room = f'R{r}_{c}'
            x = c * (ROOM_SIZE + MARGIN) + MARGIN
            y = r * (ROOM_SIZE + MARGIN) + MARGIN
            rect = pygame.Rect(x, y, ROOM_SIZE, ROOM_SIZE)

            # Determine color
            if room in obstacles:
                color = OBSTACLE_COLOR
            elif room == current:
                color = GUARD_COLOR
            elif room == alarm:
                color = ALARM_COLOR
            elif bfs_path and room in bfs_path:
                color = BFS_COLOR
            elif room in visited:
                color = VISITED_COLOR
            else:
                color = ROOM_COLOR

            pygame.draw.rect(screen, color, rect, border_radius=6)
            pygame.draw.rect(screen, GRID_LINE_COLOR, rect, width=1, border_radius=6)

    pygame.display.flip()

def animate_path(screen, path, visited, alarm=None, bfs_path=None, obstacles=None):
    for room in path:
        draw_grid(screen, visited, current=room, alarm=alarm, bfs_path=bfs_path,obstacles=obstacles)
        time.sleep(1 / FPS)
