import heapq
import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

UNWEIGHTED_GRAPH = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C', 'G'],
    'G': ['E', 'F'],
}

WEIGHTED_GRAPH = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('G', 8)],
    'E': [('B', 5), ('G', 2)],
    'F': [('C', 3), ('G', 6)],
    'G': [('D', 8), ('E', 2), ('F', 6)],
}

HEURISTIC = {
    'A': 9, 'B': 7, 'C': 6,
    'D': 5, 'E': 2, 'F': 4,
    'G': 0,
}

START = 'A'
GOAL  = 'G'


def bfs(graph, start, goal):
    t0 = time.perf_counter()
    queue = deque([[start]])
    visited = {start}
    nodes_explored = 0

    while queue:
        path = queue.popleft()
        node = path[-1]
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored, time.perf_counter() - t0

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])

    return None, nodes_explored, time.perf_counter() - t0


def dfs(graph, start, goal):
    t0 = time.perf_counter()
    stack = [[start]]
    visited = {start}
    nodes_explored = 0

    while stack:
        path = stack.pop()
        node = path[-1]
        nodes_explored += 1

        if node == goal:
            return path, nodes_explored, time.perf_counter() - t0

        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(path + [neighbour])

    return None, nodes_explored, time.perf_counter() - t0


def ucs(graph, start, goal):
    t0 = time.perf_counter()
    heap = [(0, start, [start])]
    visited = {}
    nodes_explored = 0

    while heap:
        cost, node, path = heapq.heappop(heap)
        nodes_explored += 1

        if node in visited:
            continue
        visited[node] = cost

        if node == goal:
            return path, cost, nodes_explored, time.perf_counter() - t0

        for neighbour, weight in graph.get(node, []):
            if neighbour not in visited:
                heapq.heappush(heap, (cost + weight, neighbour, path + [neighbour]))

    return None, float('inf'), nodes_explored, time.perf_counter() - t0


def greedy_best_first(graph, start, goal, heuristic):
    t0 = time.perf_counter()
    heap = [(heuristic[start], 0, start, [start])]
    visited = set()
    nodes_explored = 0

    while heap:
        h, cost, node, path = heapq.heappop(heap)
        nodes_explored += 1

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, cost, nodes_explored, time.perf_counter() - t0

        for neighbour, weight in graph.get(node, []):
            if neighbour not in visited:
                heapq.heappush(heap, (heuristic[neighbour], cost + weight, neighbour, path + [neighbour]))

    return None, float('inf'), nodes_explored, time.perf_counter() - t0


def a_star(graph, start, goal, heuristic):
    t0 = time.perf_counter()
    heap = [(heuristic[start], 0, start, [start])]
    visited = {}
    nodes_explored = 0

    while heap:
        f, g, node, path = heapq.heappop(heap)
        nodes_explored += 1

        if node in visited:
            continue
        visited[node] = g

        if node == goal:
            return path, g, nodes_explored, time.perf_counter() - t0

        for neighbour, weight in graph.get(node, []):
            if neighbour not in visited:
                new_g = g + weight
                new_f = new_g + heuristic[neighbour]
                heapq.heappush(heap, (new_f, new_g, neighbour, path + [neighbour]))

    return None, float('inf'), nodes_explored, time.perf_counter() - t0


def count_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts


def random_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]


def hill_climbing(n=8, max_restarts=50):
    t0 = time.perf_counter()
    nodes_explored = 0
    best_board = None
    best_conflicts = float('inf')

    for _ in range(max_restarts):
        board = random_board(n)
        current_conflicts = count_conflicts(board)

        while True:
            nodes_explored += 1
            improved = False

            for col in range(n):
                original_row = board[col]
                for row in range(n):
                    if row == original_row:
                        continue
                    board[col] = row
                    new_conflicts = count_conflicts(board)
                    if new_conflicts < current_conflicts:
                        current_conflicts = new_conflicts
                        original_row = row
                        improved = True
                board[col] = original_row

            if not improved:
                break

        if current_conflicts < best_conflicts:
            best_conflicts = current_conflicts
            best_board = board[:]

        if best_conflicts == 0:
            break

    return best_board, best_conflicts, nodes_explored, time.perf_counter() - t0


def simulated_annealing(n=8, initial_temp=100.0, cooling_rate=0.995, min_temp=0.01):
    t0 = time.perf_counter()
    board = random_board(n)
    current_conflicts = count_conflicts(board)
    best_board = board[:]
    best_conflicts = current_conflicts
    temp = initial_temp
    nodes_explored = 0

    while temp > min_temp:
        nodes_explored += 1
        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)
        old_row = board[col]
        board[col] = row
        new_conflicts = count_conflicts(board)
        delta = new_conflicts - current_conflicts

        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_conflicts = new_conflicts
            if current_conflicts < best_conflicts:
                best_conflicts = current_conflicts
                best_board = board[:]
        else:
            board[col] = old_row

        temp *= cooling_rate
        if best_conflicts == 0:
            break

    return best_board, best_conflicts, nodes_explored, time.perf_counter() - t0


def _bt_is_safe(board, row, col):
    for prev_col in range(col):
        if (board[prev_col] == row or
                abs(board[prev_col] - row) == abs(prev_col - col)):
            return False
    return True


def _bt_solve(board, col, n, counter):
    if col == n:
        return True
    for row in range(n):
        counter[0] += 1
        if _bt_is_safe(board, row, col):
            board[col] = row
            if _bt_solve(board, col + 1, n, counter):
                return True
            board[col] = -1
    return False


def backtracking_nqueens(n=8):
    t0 = time.perf_counter()
    board = [-1] * n
    counter = [0]
    solved = _bt_solve(board, 0, n, counter)
    return (board if solved else None), counter[0], time.perf_counter() - t0


def _fc_solve(board, col, n, domains, counter):
    if col == n:
        return True
    for row in list(domains[col]):
        counter[0] += 1
        board[col] = row
        saved = {}
        consistent = True

        for next_col in range(col + 1, n):
            saved[next_col] = set(domains[next_col])
            domains[next_col] = {
                r for r in domains[next_col]
                if r != row and abs(r - row) != abs(next_col - col)
            }
            if not domains[next_col]:
                consistent = False
                break

        if consistent and _fc_solve(board, col + 1, n, domains, counter):
            return True

        for next_col in saved:
            domains[next_col] = saved[next_col]
        board[col] = -1

    return False


def forward_checking_nqueens(n=8):
    t0 = time.perf_counter()
    board = [-1] * n
    domains = [set(range(n)) for _ in range(n)]
    counter = [0]
    solved = _fc_solve(board, 0, n, domains, counter)
    return (board if solved else None), counter[0], time.perf_counter() - t0


def run_all_and_compare():
    print("=" * 65)
    print("  Practical 2 - Search Algorithm Performance Evaluation")
    print("  Student: Pankaj Shinde  |  PRN: 202401100005")
    print("=" * 65)

    print(f"\nGraph Problem  |  Start: {START}  ->  Goal: {GOAL}\n")

    bfs_path, bfs_nodes, bfs_time                    = bfs(UNWEIGHTED_GRAPH, START, GOAL)
    dfs_path, dfs_nodes, dfs_time                    = dfs(UNWEIGHTED_GRAPH, START, GOAL)
    ucs_path, ucs_cost,  ucs_nodes, ucs_time         = ucs(WEIGHTED_GRAPH, START, GOAL)
    gbf_path, gbf_cost,  gbf_nodes, gbf_time         = greedy_best_first(WEIGHTED_GRAPH, START, GOAL, HEURISTIC)
    ast_path, ast_cost,  ast_nodes, ast_time         = a_star(WEIGHTED_GRAPH, START, GOAL, HEURISTIC)

    graph_results = [
        ("BFS",        bfs_path, "N/A",    bfs_nodes, bfs_time),
        ("DFS",        dfs_path, "N/A",    dfs_nodes, dfs_time),
        ("UCS",        ucs_path, ucs_cost, ucs_nodes, ucs_time),
        ("Greedy BFS", gbf_path, gbf_cost, gbf_nodes, gbf_time),
        ("A*",         ast_path, ast_cost, ast_nodes, ast_time),
    ]

    print(f"{'Algorithm':<14} {'Path':<25} {'Cost':<6} {'Nodes':>7} {'Time(s)':>10}")
    print("-" * 65)
    for name, path, cost, nodes, t in graph_results:
        path_str = " -> ".join(path) if path else "No solution"
        print(f"{name:<14} {path_str:<25} {str(cost):<6} {nodes:>7} {t:>10.6f}")

    N = 8
    print(f"\nN-Queens Problem  (N = {N})\n")

    hc_board, hc_conf, hc_nodes, hc_time = hill_climbing(N)
    sa_board, sa_conf, sa_nodes, sa_time = simulated_annealing(N)
    bt_board, bt_nodes, bt_time          = backtracking_nqueens(N)
    fc_board, fc_nodes, fc_time          = forward_checking_nqueens(N)

    nq_results = [
        ("Hill Climbing",    hc_board, hc_conf,                                    hc_nodes, hc_time),
        ("Simul. Annealing", sa_board, sa_conf,                                    sa_nodes, sa_time),
        ("Backtracking",     bt_board, count_conflicts(bt_board) if bt_board else "N/A", bt_nodes, bt_time),
        ("Forward Checking", fc_board, count_conflicts(fc_board) if fc_board else "N/A", fc_nodes, fc_time),
    ]

    print(f"{'Algorithm':<20} {'Board (col->row)':<35} {'Conflicts':>9} {'Nodes':>8} {'Time(s)':>10}")
    print("-" * 85)
    for name, board, conf, nodes, t in nq_results:
        board_str = str(board) if board else "No solution"
        print(f"{name:<20} {board_str:<35} {str(conf):>9} {nodes:>8} {t:>10.6f}")

    _plot_graph_algorithms(graph_results)
    _plot_nqueens_algorithms(nq_results)

    print("\nPlots saved to 'screenshots/' directory.")
    print("=" * 65)


def _plot_graph_algorithms(results):
    names = [r[0] for r in results]
    nodes = [r[3] for r in results]
    times = [r[4] * 1000 for r in results]
    costs = [r[2] if isinstance(r[2], (int, float)) else 0 for r in results]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Graph Search Algorithms - Performance Comparison", fontsize=13, fontweight='bold')
    colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B2']

    axes[0].bar(names, nodes, color=colors)
    axes[0].set_title("Nodes Explored")
    axes[0].set_ylabel("Count")
    axes[0].set_xlabel("Algorithm")

    axes[1].bar(names, times, color=colors)
    axes[1].set_title("Execution Time (ms)")
    axes[1].set_ylabel("Milliseconds")
    axes[1].set_xlabel("Algorithm")

    axes[2].bar(names, costs, color=colors)
    axes[2].set_title("Path Cost (0 = N/A)")
    axes[2].set_ylabel("Cost")
    axes[2].set_xlabel("Algorithm")

    plt.tight_layout()
    plt.savefig("screenshots/graph_algorithms_comparison.png", dpi=150)
    plt.show()


def _plot_nqueens_algorithms(results):
    names = [r[0] for r in results]
    nodes = [r[3] for r in results]
    times = [r[4] * 1000 for r in results]
    confs = [r[2] if isinstance(r[2], int) else 0 for r in results]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("N-Queens Algorithms - Performance Comparison", fontsize=13, fontweight='bold')
    colors = ['#4C72B0', '#DD8452', '#55A868', '#C44E52']

    axes[0].bar(names, nodes, color=colors)
    axes[0].set_title("Nodes / States Explored")
    axes[0].set_ylabel("Count")
    axes[0].set_xlabel("Algorithm")

    axes[1].bar(names, times, color=colors)
    axes[1].set_title("Execution Time (ms)")
    axes[1].set_ylabel("Milliseconds")
    axes[1].set_xlabel("Algorithm")

    axes[2].bar(names, confs, color=colors)
    axes[2].set_title("Conflicts in Final Solution")
    axes[2].set_ylabel("Conflicts")
    axes[2].set_xlabel("Algorithm")

    plt.tight_layout()
    plt.savefig("screenshots/nqueens_algorithms_comparison.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    random.seed(42)
    np.random.seed(42)
    run_all_and_compare()
