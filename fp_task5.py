#Final project task5
'''
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому
графі, використовуючи бінарну купу. Завдання включає створення графа,
використання піраміди для оптимізації вибору вершин та обчислення 
найкоротших шляхів від початкової вершини до всіх інших.
'''

import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(node):
    if node is None:
        return []
    stack = [node]
    visited = []
    while stack:
        current = stack.pop()
        visited.append(current)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return visited

def bfs(node):
    if node is None:
        return []
    queue = deque([node])
    visited = []
    while queue:
        current = queue.popleft()
        visited.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return visited

def generate_color(index, total):
    # Generate color from dark to light shades of blue
    shade = int(255 - (255 / total) * index)
    return f'#{shade:02x}{shade:02x}FF'

def update_node_colors(visited):
    for i, node in enumerate(visited):
        node.color = generate_color(i, len(visited))

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обхід DFS
dfs_visited = dfs(root)
update_node_colors(dfs_visited)
print("DFS Traversal Order:", [node.val for node in dfs_visited])
draw_tree(root)

# Скидання кольорів вузлів для BFS
for node in dfs_visited:
    node.color = "#1296F0"

# Обхід BFS
bfs_visited = bfs(root)
update_node_colors(bfs_visited)
print("BFS Traversal Order:", [node.val for node in bfs_visited])
draw_tree(root)
