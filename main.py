import tkinter as tk
from collections import deque
import heapq
import time # لقياس الوقت المستغرق

# تمثيل المتاهة (0 ممر، 1 جدار)
MAZE = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
START = (0, 0)
GOAL = (4, 4)

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Pathfinding Performance")
        self.cell_size = 60
        self.canvas = tk.Canvas(root, width=300, height=350)
        self.canvas.pack()
        self.info_text = self.canvas.create_text(150, 320, text="Select an algorithm")
        self.draw_maze()
        
        tk.Button(root, text="Run BFS", command=self.run_bfs).pack(side=tk.LEFT, padx=10)
        tk.Button(root, text="Run A*", command=self.run_astar).pack(side=tk.RIGHT, padx=10)
        tk.Button(root, text="Run DFS", command=self.run_dfs).pack(side=tk.BOTTOM, pady=5)
        tk.Button(root, text="Run GBFS", command=self.run_gbfs).pack(side=tk.BOTTOM, pady=5)



    def draw_maze(self):
        for r in range(len(MAZE)):
            for c in range(len(MAZE[0])):
                color = "white" if MAZE[r][c] == 0 else "black"
                if (r, c) == START: color = "green"
                if (r, c) == GOAL: color = "red"
                self.canvas.create_rectangle(c*self.cell_size, r*self.cell_size, 
                                           (c+1)*self.cell_size, (r+1)*self.cell_size, 
                                           fill=color, outline="gray")

    def run_bfs(self):
        start_time = time.time() #
        nodes_explored = 0
        queue = deque([START])
        visited = {START: None}
        
        while queue:
            curr = queue.popleft()
            nodes_explored += 1 # زيادة العداد عند فحص كل عقدة
            if curr == GOAL: break
            
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                r, c = curr[0]+dr, curr[1]+dc
                if 0 <= r < 5 and 0 <= c < 5 and MAZE[r][c] == 0 and (r,c) not in visited:
                    visited[(r,c)] = curr
                    queue.append((r,c))
        
        end_time = (time.time() - start_time) * 1000 # تحويل إلى ميلي ثانية
        self.update_stats("BFS", nodes_explored, end_time)
        self.reconstruct_path(visited)


    def run_dfs(self):
     start_time = time.time()
     nodes_explored = 0

     stack = [START]              # Stack بدل Queue
     visited = {START: None}

     while stack:
        curr = stack.pop()       # LIFO
        nodes_explored += 1

        if curr == GOAL:
            break

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            r, c = curr[0] + dr, curr[1] + dc
            next_node = (r, c)

            if 0 <= r < 5 and 0 <= c < 5:
                if MAZE[r][c] == 0 and next_node not in visited:
                    visited[next_node] = curr
                    stack.append(next_node)

     end_time = (time.time() - start_time) * 1000
     self.update_stats("DFS", nodes_explored, end_time)
     self.reconstruct_path(visited)


    def run_astar(self):
        start_time = time.time()
        nodes_explored = 0
        def heuristic(a, b): 
            return abs(a[0] - b[0]) + abs(a[1] - b[1]) # Manhattan Distance
            
        pq = [(0, START)]
        visited = {START: None}
        cost_so_far = {START: 0}
        
        while pq:
            _, curr = heapq.heappop(pq)
            nodes_explored += 1
            if curr == GOAL: break
            
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                next_node = (curr[0]+dr, curr[1]+dc)
                if 0 <= next_node[0] < 5 and 0 <= next_node[1] < 5 and MAZE[next_node[0]][next_node[1]] == 0:
                    new_cost = cost_so_far[curr] + 1
                    if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                        cost_so_far[next_node] = new_cost
                        priority = new_cost + heuristic(GOAL, next_node)
                        heapq.heappush(pq, (priority, next_node))
                        visited[next_node] = curr
        
        end_time = (time.time() - start_time) * 1000
        self.update_stats("A*", nodes_explored, end_time)
        self.reconstruct_path(visited)

    def update_stats(self, algo, nodes, exec_time):
        """تحديث بيانات الأداء على الشاشة"""
        stats = f"{algo} -> Nodes: {nodes}, Time: {exec_time:.2f}ms"
        self.canvas.itemconfig(self.info_text, text=stats)
    
    def run_gbfs(self):
     start_time = time.time()
     nodes_explored = 0
    
     def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

     pq = [(heuristic(START, GOAL), START)]  # Priority Queue
     visited = {START: None}
     explored = set()

     while pq:
        _, curr = heapq.heappop(pq)

        if curr in explored:
            continue

        explored.add(curr)
        nodes_explored += 1

        if curr == GOAL:
            break

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            r, c = curr[0] + dr, curr[1] + dc
            next_node = (r, c)

            if 0 <= r < 5 and 0 <= c < 5:
                if MAZE[r][c] == 0 and next_node not in visited:
                    visited[next_node] = curr
                    priority = heuristic(next_node, GOAL)
                    heapq.heappush(pq, (priority, next_node))

     end_time = (time.time() - start_time) * 1000
     self.update_stats("GBFS", nodes_explored, end_time)
     self.reconstruct_path(visited)


    def reconstruct_path(self, visited):
        path = []
        curr = GOAL
        while curr:
            path.append(curr)
            curr = visited.get(curr)
        self.animate_path(path[::-1])

    def animate_path(self, path):
        for node in path:
            if node != START and node != GOAL:
                r, c = node
                self.canvas.create_oval(c*self.cell_size+20, r*self.cell_size+20, 
                                      (c+1)*self.cell_size-20, (r+1)*self.cell_size-20, 
                                      fill="blue")
                self.root.update()
                self.root.after(100)

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeApp(root)
    root.mainloop()