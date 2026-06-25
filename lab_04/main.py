def window_hash(s: str, m: int) -> int:
    """
    Вычисляет полиномиальный хэш (основание 31) первых m символов строки s.
    
    Правила обработки:
      - Если m <= 0, возвращается 0.
      - Если m > len(s), хэш вычисляется для всей строки (m принудительно усекается до len(s)).
      - Если передан неверный тип аргументов, выбрасывается TypeError.
    
    Формула: H = sum(ord(s[i]) * 31^(m-1-i)) для i от 0 до m-1.
    """
    # Проверка типов
    if not isinstance(s, str):
        raise TypeError("Аргумент 's' должен быть строкой")
    if not isinstance(m, int):
        raise TypeError("Аргумент 'm' должен быть целым числом")
    
    # Обработка граничных значений m
    if m <= 0:
        return 0
    if m > len(s):
        m = len(s)          # хэшируем всю строку, если запрошено больше символов, чем есть
    
    p = 31
    h = 0
    # Степень p^(m-1-i) вычисляется на лету; можно предварительно вычислить степени, но это необязательно
    for i in range(m):
        h += ord(s[i]) * (p ** (m - 1 - i))
    return h


# ===== Блок для тестирования (можно удалить при сдаче) =====
if __name__ == "__main__":
    # Корректные вызовы
    print("window_hash('ABC', 3) =", window_hash("ABC", 3))   # 65*31^2 + 66*31 + 67 = 64578
    print("window_hash('ABC', 2) =", window_hash("ABC", 2))   # 65*31 + 66 = 2081
    print("window_hash('Hello', 10) =", window_hash("Hello", 10))  # m > len -> хэш всей строки
    
    # Неправильные, но обрабатываемые значения
    print("window_hash('test', 0) =", window_hash("test", 0))     # 0
    print("window_hash('test', -3) =", window_hash("test", -3))   # 0
    print("window_hash('', 5) =", window_hash("", 5))             # 0, т.к. len=0, m усекается до 0
    
    # Попытка передать нестроку вызовет исключение (раскомментируйте для проверки)
    # print(window_hash(123, 2))   # TypeError
