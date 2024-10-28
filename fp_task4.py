#Final project task4
'''
Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
Примітка. Суть завдання полягає у створенні дерева із купи.
'''


import uuid
import heapq

import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    
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
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

def create_tree_from_heap(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = Node(arr[i])
        root = temp

        # Insert left child
        root.left = create_tree_from_heap(arr, root.left, 2 * i + 1, n)

        # Insert right child
        root.right = create_tree_from_heap(arr, root.right, 2 * i + 2, n)

    return root

heap_data = [0, 4 , 5, 10, 1, 3]
heapq.heapify(heap_data)
print(heap_data)

n = len(heap_data)
root = None

root = create_tree_from_heap(heap_data, root, 0, n)

# Відображення дерева
draw_tree(root)