import heapq

graph = {
    'Червоний університет': {'Михайлівський собор': {'is_direct': False, 'weight': 1.4}, 'Київська політехніка': {'is_direct': False, 'weight': 2.1}},
    'Андріївська церква': {'Михайлівський собор': {'is_direct': True, 'weight': 1.1}},
    'Михайлівський собор': {'Софія київська': {'is_direct': True, 'weight': 1.2}, 'Фунікулер': {'is_direct': False, 'weight': 0.8}},
    'Золоті ворота': {'Фонтан на Хрещатику': {'is_direct': True, 'weight': 1.8}},
    'Лядські ворота': {'Михайлівський собор': {'is_direct': True, 'weight': 1.6}},
    'Фунікулер': {'Музей однієї вулиці': {'is_direct': True, 'weight': 0.4}},
    'Київська політехніка': {},
    'Фонтан на Хрещатику': {'Національна філармонія': {'is_direct': False, 'weight': 0.5}},
    'Софія київська': {'Лядські ворота': {'is_direct': True, 'weight': 0.8}},
    'Національна філармонія': {'Київська політехніка': {'is_direct': False, 'weight': 4.7}},
    'Музей однієї вулиці': {}
}

def find_path_terri(graph, start, end):
    # Инициализация посещенных вершин, очереди и пути
    visited = set()
    queue = [(start, [], {})]
    path = []

    # Цикл выполняется, пока очередь не пуста
    while queue:
        # Извлечение вершины, пути и направлений ребер из очереди
        (node, path, edge_directions) = queue.pop(0)

        # Если вершина еще не была посещена
        if node not in visited:
            # Добавление вершины в посещенные
            visited.add(node)
            # Добавление вершины в путь
            path = path + [node]

            # Если текущая вершина равна конечной вершине
            if node == end:
                # Прерывание цикла
                break

            # Обход соседних вершин текущей вершины
            for neighbor in graph[node].keys():
                # Создание копии словаря с направлениями ребер
                new_edge_directions = edge_directions.copy()

                # Формирование ключей для ребра и обратного ребра
                edge_key = (node, neighbor)
                reverse_edge_key = (neighbor, node)

                # Если ребро не было пройдено или было пройдено в обратном направлении
                if edge_key not in new_edge_directions or new_edge_directions[edge_key] == -1:
                    # Отметка направления ребра
                    new_edge_directions[edge_key] = 1
                    if reverse_edge_key in new_edge_directions:
                        new_edge_directions[reverse_edge_key] = -1

                    # Добавление соседней вершины, обновленного пути и направлений ребер в очередь
                    queue.append((neighbor, path, new_edge_directions))

    # Возврат найденного пути
    return path


def find_path_dijkstra(graph, start, end):
    # Find the shortest path from start to end in the graph using Dijkstra's algorithm
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    previous = {}

    while priority_queue:
        (current_distance, current_node) = heapq.heappop(priority_queue)
        if current_node in visited:
            continue

        visited.add(current_node)
        if current_node == end:
            break

        for neighbor, edge in graph[current_node].items():
            new_distance = current_distance + edge['weight']
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
                previous[neighbor] = current_node

    if end not in previous:
        return []

    path = [end]
    while path[-1] != start:
        path.append(previous[path[-1]])
    path.reverse()

    return path


def find_path(graph, start, end):
    # Find the shortest path from start to end in the graph
    visited = set()
    queue = [(start, [])]
    path = []

    while queue:
        (node, path) = queue.pop(0)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                break
            queue.extend([(neighbor, path) for neighbor in graph[node].keys()])

    return path


def max_cars(graph, path):
    max_cars = 400
    for i in range(len(path) - 1):
        edge = graph[path[i]][path[i+1]]
        if edge['is_direct']:
            max_cars = min(max_cars, 400 * edge['weight'])

    return max_cars

start = "Червоний університет"
end = "Музей однієї вулиці"


result = max_cars(graph,
                  find_path_dijkstra(graph, start, end)
                  )
print(f"Maximum number of cars that can reach the {end} from {start}: {result}")