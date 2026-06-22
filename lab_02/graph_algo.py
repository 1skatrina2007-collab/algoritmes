"""Реализация представления графа и поиска компонент связности.

Вариант 19: 7 вершин, ребра (1,2), (2,3), (3,4), (4,5), (5,6), (6,7).
"""

from typing import List, Tuple


def build_adjacency_matrix(num_vertices: int,
                           edges: List[Tuple[int, int]]) -> List[List[int]]:
    """Строит матрицу смежности по числу вершин и списку ребер.

    Вершины нумеруются с 1, в матрице используется индексация с 0.
    Граф считается неориентированным, поэтому A[i][j] == A[j][i].

    Сложность: O(V^2) на создание матрицы + O(E) на заполнение.
    """
    matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v in edges:
        matrix[u - 1][v - 1] = 1
        matrix[v - 1][u - 1] = 1
    return matrix


def build_incidence_matrix(num_vertices: int,
                           edges: List[Tuple[int, int]]) -> List[List[int]]:
    """Строит матрицу инцидентности размера V x E.

    Столбец соответствует ребру, в строках соединяемых вершин стоит 1.

    Сложность: O(V * E).
    """
    num_edges = len(edges)
    matrix = [[0] * num_edges for _ in range(num_vertices)]
    for col, (u, v) in enumerate(edges):
        matrix[u - 1][col] = 1
        matrix[v - 1][col] = 1
    return matrix


def find_connected_components(num_vertices: int,
                              adjacency: List[List[int]]) -> List[List[int]]:
    """Находит компоненты связности обходом в глубину (DFS).

    Возвращает список компонент, каждая компонента — список вершин (с 1).

    Сложность: O(V^2) при матрице смежности (для каждой вершины
    просматривается строка длины V).
    """
    visited = [False] * num_vertices
    components: List[List[int]] = []

    def dfs(start: int, component: List[int]) -> None:
        stack = [start]
        visited[start] = True
        while stack:
            node = stack.pop()
            component.append(node + 1)
            for neighbour in range(num_vertices):
                if adjacency[node][neighbour] == 1 and not visited[neighbour]:
                    visited[neighbour] = True
                    stack.append(neighbour)

    for vertex in range(num_vertices):
        if not visited[vertex]:
            component: List[int] = []
            dfs(vertex, component)
            components.append(sorted(component))
    return components


def print_matrix(matrix: List[List[int]], title: str) -> None:
    """Печатает матрицу с заголовком."""
    print(title)
    for row in matrix:
        print(" ".join(str(value) for value in row))
    print()
