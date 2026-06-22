"""Бинарное дерево поиска (BST) и пирамидальная сортировка (Heap Sort).

Вариант 19:
  Дерево: {21, 13, 29, 11, 18, 25, 32}, найти 25, удалить 21.
  Куча:   [21, 13, 29, 11, 18, 25, 32].
"""

from typing import List, Optional


class Node:
    """Узел бинарного дерева поиска."""

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BST:
    """Бинарное дерево поиска.

    Операции (в среднем для сбалансированного дерева):
      insert  — O(log n)
      search  — O(log n)
      delete  — O(log n)
    В худшем случае (вырожденное дерево) — O(n).
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """Вставляет значение в дерево."""
        self.root = self._insert(self.root, value)

    def _insert(self, node: Optional[Node], value: int) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    def search(self, value: int) -> bool:
        """Возвращает True, если значение присутствует в дереве."""
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def delete(self, value: int) -> None:
        """Удаляет значение из дерева.

        При двух потомках узел заменяется минимальным элементом
        правого поддерева (преемником).
        """
        self.root = self._delete(self.root, value)

    def _delete(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    @staticmethod
    def _min_node(node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def inorder(self) -> List[int]:
        """Симметричный обход — возвращает отсортированный список значений."""
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[Node], result: List[int]) -> None:
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)


def _heapify(array: List[int], heap_size: int, root: int) -> None:
    """Восстанавливает свойство max-heap для поддерева с корнем root."""
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < heap_size and array[left] > array[largest]:
        largest = left
    if right < heap_size and array[right] > array[largest]:
        largest = right
    if largest != root:
        array[root], array[largest] = array[largest], array[root]
        _heapify(array, heap_size, largest)


def heap_sort(array: List[int], verbose: bool = False) -> List[int]:
    """Сортирует массив пирамидальной сортировкой по возрастанию.

    Сложность: O(n log n) во всех случаях, память O(1) (in-place).
    """
    data = list(array)
    n = len(data)

    # Построение max-heap.
    for i in range(n // 2 - 1, -1, -1):
        _heapify(data, n, i)
    if verbose:
        print(f"После построения max-heap: {data}")

    # Извлечение элементов из кучи.
    for end in range(n - 1, 0, -1):
        data[0], data[end] = data[end], data[0]
        _heapify(data, end, 0)
        if verbose:
            print(f"Шаг (зафиксирован индекс {end}): {data}")

    return data
