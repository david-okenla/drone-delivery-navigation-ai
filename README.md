# Drone Delivery Navigation — AI Search Algorithms

A Python implementation of **BFS, DFS, UCS, and A\*** applied to an autonomous drone delivery problem, where a city is modelled as a weighted graph and the goal is to find the optimal path from a warehouse to a customer.

> **Course:** Artificial Intelligence  
> **Assignment:** Take-Home Assignment 1 — Advanced Drone Delivery Navigation

---

## Problem Overview

A logistics company uses autonomous drones to deliver packages across a city. The city is represented as a graph where:
- **Nodes** = intersections / locations
- **Edges** = roads with travel times (in minutes)
- **Constraints** = limited battery life, traffic delays

The task is to find the shortest-time path from a start node (`A`) to a goal node (`H`).

---

## Graph & Heuristic

```
Nodes: A, B, C, D, E, F, G, H
Start: A  |  Goal: H
```

| Algorithm | Explores based on |
|-----------|------------------|
| DFS       | Depth (stack) — no cost awareness |
| BFS       | Fewest hops (queue) — no cost awareness |
| UCS       | Cumulative edge cost (min-heap) |
| A*        | Cost + heuristic estimate to goal |

---

## Results

| Algorithm | Path | Steps | Cost |
|-----------|------|-------|------|
| DFS  | A → B → D → C → F → G → H | 6 | 13 |
| BFS  | A → B → E → G → H         | 4 | 10 |
| UCS  | A → D → E → G → H         | 4 | **7** |
| A*   | A → D → E → G → H         | 4 | **7** |

UCS and A* find the optimal (lowest-cost) path. A* does so while expanding fewer nodes thanks to the heuristic.

---

## Files

| File | Description |
|------|-------------|
| `assignment_starter_code.py` | Main implementation — all four algorithms |

---

## How to Run

```bash
python assignment_starter_code.py
```

No external dependencies — uses only Python's built-in `heapq` and `collections` modules.

---

## Algorithms Implemented

- **DFS** — recursive, with backtracking
- **BFS** — iterative, using `collections.deque`
- **UCS** — iterative, using `heapq` ordered by path cost `g`
- **A\*** — iterative, using `heapq` ordered by `f = g + h`
