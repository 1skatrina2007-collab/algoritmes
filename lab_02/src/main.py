"""Запуск задач лабораторной работы №2, вариант 19.

Граф:   7 вершин, ребра (1,2), (2,3), (3,4), (4,5), (5,6), (6,7).
Дерево: {21, 13, 29, 11, 18, 25, 32}; найти 25, удалить 21.
Куча:   [21, 13, 29, 11, 18, 25, 32].
"""

from src.graph_algo import (
    build_adjacency_matrix,
    build_incidence_matrix,
    find_connected_components,
    print_matrix,
)
from src.tree_algo import BST, heap_sort


NUM_VERTICES = 7
EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
TREE_ELEMENTS = [21, 13, 29, 11, 18, 25, 32]
SEARCH_VALUE = 25
DELETE_VALUE = 21
HEAP_ARRAY = [21, 13, 29, 11, 18, 25, 32]


def run_graph() -> None:
    print("=" * 50)
    print("ГРАФ (вариант 19)")
    print("=" * 50)
    print(f"Вершины: {NUM_VERTICES}")
    print(f"Ребра:   {EDGES}\n")

    adjacency = build_adjacency_matrix(NUM_VERTICES, EDGES)
    incidence = build_incidence_matrix(NUM_VERTICES, EDGES)

    print_matrix(adjacency, "Матрица смежности:")
    print_matrix(incidence, "Матрица инцидентности:")

    components = find_connected_components(NUM_VERTICES, adjacency)
    print(f"Количество компонент связности: {len(components)}")
    for index, component in enumerate(components, start=1):
        print(f"  Компонента {index}: {component}")
    print()


def run_tree() -> None:
    print("=" * 50)
    print("БИНАРНОЕ ДЕРЕВО ПОИСКА (вариант 19)")
    print("=" * 50)
    print(f"Элементы для вставки: {TREE_ELEMENTS}\n")

    tree = BST()
    for value in TREE_ELEMENTS:
        tree.insert(value)

    print(f"Симметричный обход (отсортировано): {tree.inorder()}")

    found = tree.search(SEARCH_VALUE)
    print(f"Поиск значения {SEARCH_VALUE}: "
          f"{'найдено' if found else 'не найдено'}")

    print(f"Удаление значения {DELETE_VALUE}...")
    tree.delete(DELETE_VALUE)
    print(f"Обход после удаления: {tree.inorder()}\n")


def run_heap_sort() -> None:
    print("=" * 50)
    print("ПИРАМИДАЛЬНАЯ СОРТИРОВКА (вариант 19)")
    print("=" * 50)
    print(f"Исходный массив: {HEAP_ARRAY}\n")

    result = heap_sort(HEAP_ARRAY, verbose=True)
    print(f"\nОтсортированный массив: {result}\n")


def main() -> None:
    run_graph()
    run_tree()
    run_heap_sort()


if __name__ == "__main__":
    main()

