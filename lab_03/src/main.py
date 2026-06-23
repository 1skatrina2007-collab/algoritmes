# =========================================================
# БЛОК 1. АЛГОРИТМЫ ПОИСКА
# =========================================================

def linear_search(arr, target):
    """Линейный поиск числа. Индекс первого вхождения или -1."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_str(arr, target):
    """Линейный поиск строки (регистрозависимый). Индекс или -1."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """Классический бинарный поиск в отсортированном массиве. Индекс или -1."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_transaction(ids, target_id):
    """Бизнес: поиск ID транзакции бинарным поиском за O(log n)."""
    left, right = 0, len(ids) - 1
    while left <= right:
        mid = (left + right) // 2
        if ids[mid] == target_id:
            return mid
        elif ids[mid] < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_overdue_payment(delays, limit):
    """Бизнес: индекс первого клиента, чья просрочка строго больше limit, иначе -1."""
    for i in range(len(delays)):
        if delays[i] > limit:
            return i
    return -1


# =========================================================
# БЛОК 2. ПУЗЫРЬКОВАЯ СОРТИРОВКА
# =========================================================

def bubble_sort(arr):
    """Сортировка пузырьком по возрастанию (in-place)."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_desc_len(arr):
    """Сортировка строк по убыванию длины (in-place)."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def sort_sales_data(sales):
    """Бизнес: сортировка продаж по убыванию пузырьком (in-place)."""
    n = len(sales)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if sales[j] < sales[j + 1]:
                sales[j], sales[j + 1] = sales[j + 1], sales[j]
    return sales


def bubble_sort_count_swaps(arr):
    """Пузырьковая сортировка с подсчётом перестановок (in-place)."""
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


# =========================================================
# БЛОК 3. СОРТИРОВКА ВЫБОРОМ
# =========================================================

def selection_sort(arr):
    """Сортировка выбором по возрастанию (in-place)."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def selection_sort_chars(arr):
    """Сортировка символов в алфавитном порядке методом выбора (in-place)."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def sort_competitor_prices(prices):
    """Бизнес: сортировка цен по возрастанию методом выбора (in-place)."""
    n = len(prices)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if prices[j] < prices[min_idx]:
                min_idx = j
        prices[i], prices[min_idx] = prices[min_idx], prices[i]
    return prices


def get_min_index(arr, start_index):
    """Индекс минимального элемента в arr[start_index:]."""
    min_idx = start_index
    for j in range(start_index + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    return min_idx


# =========================================================
# БЛОК 4. СОРТИРОВКА ВСТАВКАМИ
# =========================================================

def insertion_sort(arr):
    """Сортировка вставками по возрастанию (in-place)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def insertion_sort_float(arr):
    """Сортировка float-чисел методом вставок (in-place)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def sort_invoices(timestamps):
    """Бизнес: сортировка временных меток вставками (in-place)."""
    for i in range(1, len(timestamps)):
        key = timestamps[i]
        j = i - 1
        while j >= 0 and timestamps[j] > key:
            timestamps[j + 1] = timestamps[j]
            j -= 1
        timestamps[j + 1] = key
    return timestamps


def insertion_sort_optimized(arr):
    """Сортировка вставками (in-place)."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# =========================================================
# БЛОК 5. СОРТИРОВКА ШЕЛЛА И АНАЛИТИКА
# =========================================================

def shell_sort(arr):
    """Сортировка Шелла с шагом n // 2 (in-place)."""
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def sort_large_user_ids(ids):
    """Бизнес: сортировка User IDs методом Шелла (in-place)."""
    n = len(ids)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = ids[i]
            j = i
            while j >= gap and ids[j - gap] > temp:
                ids[j] = ids[j - gap]
                j -= gap
            ids[j] = temp
        gap //= 2
    return ids


def is_sorted(arr):
    """Проверка: отсортирован ли массив по возрастанию (True/False)."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# =========================================================
# ДЕМОНСТРАЦИЯ
# =========================================================

if __name__ == "__main__":
    print(linear_search([10, 50, 30, 70, 80, 20], 30))            # 2
    print(linear_search_str(["apple", "banana", "cherry"], "banana"))  # 1
    print(binary_search([1, 3, 5, 7, 9, 11], 9))                  # 4
    print(search_transaction([1001, 1005, 1010, 1025], 1010))     # 2
    print(find_overdue_payment([0, 5, 12, 3, 40], 10))            # 2

    a = [5, 2, 9, 1, 5, 6]; bubble_sort(a); print(a)             # [1, 2, 5, 5, 6, 9]
    a = ["a", "ccc", "bb"]; bubble_sort_desc_len(a); print(a)    # ['ccc', 'bb', 'a']
    a = [100.5, 50.0, 200.0]; sort_sales_data(a); print(a)       # [200.0, 100.5, 50.0]
    print(bubble_sort_count_swaps([3, 2, 1]))                    # 3
    print(bubble_sort_count_swaps([1, 2, 3]))                    # 0

    a = [64, 25, 12, 22, 11]; selection_sort(a); print(a)        # [11, 12, 22, 25, 64]
    a = ['c', 'a', 'b']; selection_sort_chars(a); print(a)       # ['a', 'b', 'c']
    a = [99.9, 45.0, 50.0]; sort_competitor_prices(a); print(a)  # [45.0, 50.0, 99.9]
    print(get_min_index([10, 50, 20, 5, 40], 1))                 # 3

    a = [12, 11, 13, 5, 6]; insertion_sort(a); print(a)          # [5, 6, 11, 12, 13]
    a = [1.1, 0.9, 1.2]; insertion_sort_float(a); print(a)       # [0.9, 1.1, 1.2]
    a = [100, 102, 101, 103]; sort_invoices(a); print(a)         # [100, 101, 102, 103]
    a = [1, 2, 3, 5, 4]; insertion_sort_optimized(a); print(a)   # [1, 2, 3, 4, 5]

    a = [12, 34, 54, 2, 3]; shell_sort(a); print(a)              # [2, 3, 12, 34, 54]
    a = [900, 100, 500, 300]; sort_large_user_ids(a); print(a)   # [100, 300, 500, 900]
    print(is_sorted([1, 2, 3, 4]))                               # True
