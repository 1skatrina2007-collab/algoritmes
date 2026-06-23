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

if __name__ == "__main__":
    print(sort_large_user_ids([900, 100, 500, 300]))