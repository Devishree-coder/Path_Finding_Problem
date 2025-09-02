import pygame
import heapq
from grid import reconstruct_path

# A* Algorithm
def astar(draw, grid, start, end):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = start.h(end)

    open_set_hash = {start}

    while open_set:
        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g = g_score[current] + 1
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + neighbor.h(end)
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False


# Dijkstra Algorithm
def dijkstra(draw, grid, start, end):
    dist = {node: float("inf") for row in grid for node in row}
    dist[start] = 0
    pq = [(0, start)]
    came_from = {}

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            new_dist = dist[current] + 1
            if new_dist < dist[neighbor]:
                came_from[neighbor] = current
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False


# BFS Algorithm
def bfs(draw, grid, start, end):
    from collections import deque
    queue = deque([start])
    came_from = {}

    while queue:
        current = queue.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in came_from and neighbor != start:
                came_from[neighbor] = current
                queue.append(neighbor)
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False


# DFS Algorithm
def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {}

    while stack:
        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            if neighbor not in came_from and neighbor != start:
                came_from[neighbor] = current
                stack.append(neighbor)
                neighbor.make_open()

        draw()
        if current != start:
            current.make_closed()

    return False
