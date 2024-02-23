"""
Модуль демонстрации использования классов ListStats и ListComparator.
"""
from list_comparator import ListComparator
from list_stats import ListStats


def main():
    """
    Предлагает пользователю два списка, вычисляет и сравнивает их средние значения.
    """

    list1_str = input("Введите элементы первого списка через запятую: ")
    list2_str = input("Введите элементы второго списка через запятую: ")

    try:
        # Преобразование входных строк в числовые списки
        list1 = [float(item) for item in list1_str.split(",")]
        list2 = [float(item) for item in list2_str.split(",")]
    except ValueError:
        print("Неверный формат данных. Пожалуйста, введите числовые значения.")
        return

    # Создайние объектов ListStats для каждого списка.
    stats1 = ListStats(list1)
    stats2 = ListStats(list2)

    # Вызов ListComparator для сравнения средних значений и вывода результата.
    comparator = ListComparator(stats1, stats2)
    comparison_result = comparator.compare_means()

    if comparison_result:
        print("Means are equal.")
    else:
        mean1 = stats1.get_mean()
        mean2 = stats2.get_mean()
        if mean1 > mean2:
            print(f"Первый список имеет большее среднее значение: {mean1}")
        else:
            print(f"Второй список имеет большее среднее значение: {mean2}")


if __name__ == "__main__":
    main()
