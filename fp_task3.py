#Final project task3
'''
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому
графі, використовуючи бінарну купу. Завдання включає створення графа,
використання піраміди для оптимізації вибору вершин та обчислення 
найкоротших шляхів від початкової вершини до всіх інших.
'''
import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('inf') for vertex in graph}
    print(distances)
    distances[start] = 0
    # Черга з пріорітетами для відвідування вершин
    priority_queue = [(0, start)]

    # Поки черга не порожня перевіряємо вершини та їх ребра
    while priority_queue:
        # Отримати вершину з найменшим ребром
        current_distance, current_vertex = heapq.heappop(priority_queue)
        print(current_distance, current_vertex)

        # Пропускаємо якщо поточна довжина вже більша
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо сусідів
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # Опрацьовуємо тільки якщо менший
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E' : 8},
    'E': {'D': 8}
}

print(dijkstra(graph, 'A'))
    

