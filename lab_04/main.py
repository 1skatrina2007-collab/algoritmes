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

def main():
    s = input("Введите строку: ")
    try:
        m = int(input("Введите m: "))
    except ValueError:
        print("Ошибка: m должно быть целым числом")
        return
    expected = input("Введите ожидаемый хэш (или оставьте пустым для пропуска): ")
    result = window_hash(s, m)
    print(f"Исходная строка: {s}")
    print(f"m = {m}")
    print(f"Полученный хэш: {result}")
    if expected:
        print(f"Ожидаемый хэш: {expected}")
        print("Результат:", "верно" if str(result) == expected else "неверно")

if __name__ == "__main__":
    main()
