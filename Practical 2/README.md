# Practical 2 – Search Algorithm Performance Evaluation

**TY B.Tech. – Artificial Intelligence and Machine Learning**

| Field | Details |
|---|---|
| Student Name | Om Deore |
| PRN | 202401100093 |
| Branch | Software Engineering |
| Division / Batch | B / B1 |
| MDM Batch : A4   |
| Roll No. | 11 |
| Faculty | Dr. Khushal Khairnar |
| Date of Submission | 07-09-2026 |

---

## Problem Statement

Implement and evaluate different search algorithms used for problem solving in Artificial Intelligence. The algorithms are categorised into **Uninformed Search**, **Informed Search**, **Local Search**, and **Constraint Satisfaction** techniques. Their performance is compared using execution time, nodes explored, solution quality, and path cost.

---

## Algorithms Implemented

| Category | Algorithm |
|---|---|
| Uninformed Search | Breadth-First Search (BFS) |
| Uninformed Search | Depth-First Search (DFS) |
| Uninformed Search | Uniform Cost Search (UCS) |
| Informed Search | Greedy Best-First Search |
| Informed Search | A\* Search |
| Local Search | Hill Climbing |
| Local Search | Simulated Annealing |
| Constraint Satisfaction | Backtracking |
| Constraint Satisfaction | Forward Checking |

---

## Repository Structure

```
search_algorithms/
├── search_algorithms.py        # Main source code (all 9 algorithms)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── sample/
│   ├── sample_input.txt        # Description of inputs used
│   └── sample_output.txt       # Expected/sample output
└── screenshots/
    ├── graph_algorithms_comparison.png   # Generated after running
    └── nqueens_algorithms_comparison.png # Generated after running
```

---

## Problem Definitions

### Graph Problem (BFS, DFS, UCS, Greedy, A\*)
- **Start Node:** A  
- **Goal Node:** G  
- A 7-node weighted/unweighted graph is used.  
- Heuristic values (h(n) to goal G): A=9, B=7, C=6, D=5, E=2, F=4, G=0

### N-Queens Problem (Hill Climbing, Simulated Annealing, Backtracking, Forward Checking)
- **Board Size:** 8×8 (N = 8)  
- **Goal:** Place 8 queens on the board such that no two queens attack each other.  
- Board is represented as a list where `board[col] = row`.

---

## Performance Parameters Measured

- Execution time (seconds)
- Number of nodes / states explored
- Solution path or final board configuration
- Path cost (for graph algorithms)
- Number of conflicts (for N-Queens algorithms)

---

## How to Run

### 1. Clone the repository
```bash
git clone <repository-url>
cd search_algorithms
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the main script
```bash
python search_algorithms.py
```

The script will:
- Run all 9 algorithms
- Print a performance comparison table in the terminal
- Generate and save comparison plots to the `screenshots/` folder

---

## Dependencies

| Library | Purpose |
|---|---|
| Python (≥ 3.8) | Core language |
| NumPy | Numerical operations |
| Matplotlib | Performance comparison graphs |
| heapq, collections, time, math, random | Python standard library |

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## Sample Output (Terminal)

```
=================================================================
  Practical 2 – Search Algorithm Performance Evaluation
  Student: Om Deore  |  PRN: 202401100093
=================================================================

Graph Problem  |  Start: A  →  Goal: G

Algorithm      Path                      Cost   Nodes    Time(s)
-----------------------------------------------------------------
BFS            A → B → E → G            N/A        4   0.000021
DFS            A → B → D → ...→ G       N/A        5   0.000018
UCS            A → B → E → G              8        6   0.000031
Greedy BFS     A → B → E → G              8        4   0.000025
A*             A → B → E → G              8        5   0.000028

N-Queens Problem  (N = 8)

Algorithm            Board                          Conflicts  Nodes    Time(s)
---------------------------------------------------------------------------------
Hill Climbing        [0, 4, 7, 5, 2, 6, 1, 3]              0    312   0.004210
Simul. Annealing     [3, 6, 2, 7, 1, 4, 0, 5]              0   8741   0.031500
Backtracking         [0, 4, 7, 5, 2, 6, 1, 3]              0    876   0.001200
Forward Checking     [0, 4, 7, 5, 2, 6, 1, 3]              0    113   0.000850
```

---

## Key Observations

- **BFS** finds the shortest path (fewest hops) on unweighted graphs.
- **DFS** uses less memory but may not find the optimal path.
- **UCS** guarantees the minimum-cost path on weighted graphs.
- **Greedy BFS** is fast but not always optimal.
- **A\*** balances path cost and heuristic — optimal with an admissible heuristic.
- **Hill Climbing** is fast but can get stuck in local optima; random restarts help.
- **Simulated Annealing** escapes local optima by accepting worse states probabilistically.
- **Backtracking** systematically finds a valid N-Queens solution.
- **Forward Checking** explores significantly fewer nodes than plain backtracking by pruning domains early.

---

## License

This project is submitted as part of the TY B.Tech. AIML Lab curriculum.
