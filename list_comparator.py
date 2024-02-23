"""
Модуль демонстрации использования классов ListStats и ListComparator.
"""

from list_stats import ListStats


class ListComparator:
    """
    Сравнивает два объекта ListStats.
    """

    def __init__(self, list1: ListStats, list2: ListStats):
        """
        Инициализирует ListComparator двумя объектами ListStats.

        Args:
            list1: первый объект ListStats.
            list2: второй объект ListStats.
        """

        self._list1 = list1
        self._list2 = list2

    def compare_means(self) -> bool:
        """
        Сравнивает средние значения двух объектов ListStats.

        Returns:
            True, если средние значения равны в пределах допуска, в противном случае — False.
        """

        tol = 0.001
        mean1 = self._list1.get_mean()
        mean2 = self._list2.get_mean()

        if mean1 is None or mean2 is None:
            return None

        return abs(mean1 - mean2) < tol

    def compare_standard_deviations(self) -> bool:
        """
        Сравнивает стандартные отклонения двух объектов ListStats.

        Returns:
            True, если стандартные отклонения равны в пределах допуска, в противном случае — False.
        """

        tol = 0.001
        std_dev1 = self._list1.get_standard_deviation()
        std_dev2 = self._list2.get_standard_deviation()
        return abs(std_dev1 - std_dev2) < tol
