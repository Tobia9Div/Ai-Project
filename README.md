# 🤖 Robot Maze Pathfinding Solver
Course: Introduction to Artificial Intelligence (Level 3)
This project implements and compares various search algorithms to find the optimal path for a robot in a grid-based maze with obstacles.

# 🚀📋 Project Description
The goal is to navigate a robot from a Start Point (Green) to a Goal Point (Red). The project evaluates the efficiency of different AI search strategies based on time complexity, nodes explored, and path optimality.

## Algorithms Implemented
The following algorithms are implemented to solve the maze problem:

* Uninformed Search:

Breadth-First Search (BFS): Guarantees the shortest path in a uniform cost grid.

Depth-First Search (DFS): Explores paths deeply; memory-efficient but not optimal.

* Informed Search:

*A Search:** Uses Manhattan Distance heuristic to find the optimal path efficiently.


Uniform-Cost Search (UCS): Expands the cheapest node first.

Hill Climbing: A local search move-based approach toward the goal.

📊 Performance Comparison
Based on our implementation, here is a summary of how the algorithms performed on a 5x5 maze:

Algorithm,Nodes Explored,Path Length,Optimality
BFS,High,Shortest,Yes
*A (Manhattan)**,Lowest,Shortest,Yes
DFS,Variable,Long,No

## 🛠️ Installation & Usage
Requirements: Python 3.x and Tkinter library (pre-installed with Python).

## Clone the Repo:

` ` ` git clone https://github.com/your-username/maze-ai-project.git

## Run the Project:

` ` ` python main.py
