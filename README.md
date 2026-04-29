# 🏛️ Museum Guard Patrol

> An AI-powered museum guard simulation using DFS for patrol and BFS for alarm response, visualized in real-time with Pygame.

---

## 📖 Overview

**Museum Guard Patrol** simulates a security guard navigating a museum represented as a 10×10 grid graph. The guard uses **Depth-First Search (DFS)** to patrol rooms, and when an alarm is randomly triggered, switches to **Breadth-First Search (BFS)** to find the shortest path to the disturbance — all animated live using Pygame.

---

## ✨ Features

- 🗺️ **Procedural Museum Map** — Randomly generated 10×10 grid with obstacles
- 🚶 **DFS Patrol** — Guard explores the museum room by room using depth-first traversal
- 🚨 **Random Alarm Trigger** — 10% chance per room visit of triggering an alarm
- ⚡ **BFS Alarm Response** — Instantly finds the shortest path from the guard's position to the alarm room
- 📊 **Metrics Report** — Prints patrol coverage, response time, and full path details
- 🎨 **Pygame Visualization** — Color-coded live animation of the guard's movement

---

## 🗂️ Project Structure

```
MuseumGuardPatrol/
├── main.py           # Entry point — game loop & orchestration
├── BFS.py            # Breadth-First Search for alarm response
├── DFS.py            # Depth-First Search for patrol
├── map.py            # Museum graph generation with obstacles
├── visual.py         # Pygame grid drawing & path animation
├── metrics.py        # Coverage & performance reporting
├── requirements.txt  # Python dependencies
└── .gitignore
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pygame | Real-time grid visualization |
| BFS (collections.deque) | Shortest path to alarm room |
| DFS (recursion) | Room-by-room patrol traversal |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Pygame

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

## 🎨 Color Guide

| Color | Meaning |
|---|---|
| ⬜ White | Unvisited room |
| 🔵 Light Blue | DFS patrolled room |
| 🟦 Cornflower Blue | Guard's current position |
| 🔴 Tomato Red | Alarm room |
| 🟡 Gold | BFS response path |
| ⬛ Gray | Obstacle (blocked room) |

---

## 🧠 Algorithm Flow

```
Start at R0_0
      │
      ▼
  [ DFS Patrol ]
  Visit rooms one by one
  10% chance of alarm per room
      │
      ├── No alarm → continue patrol
      │
      └── Alarm triggered!
              │
              ▼
        [ BFS Response ]
        Find shortest path
        from current room → alarm room
              │
              ▼
        Animate response path
        Print metrics & coverage
```

---

## 📊 Sample Metrics Output

```
--- METRICS ---
DFS Patrol Order: ['R0_0', 'R0_1', 'R1_1', ...]
Total Rooms Patrolled (DFS): 23
Alarm Response Path (BFS): ['R1_1', 'R1_2', 'R2_2', 'R3_2']
Response Time (steps): 3
Coverage: 26.00%
```

---

## 📄 License

This project is for educational purposes.
