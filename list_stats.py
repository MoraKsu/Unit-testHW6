"""
Модуль вычисления среднего значения списка.
"""


class ListStats:
    """
    Класс для вычисления среднего значения списка.
    """

    def __init__(self, list_data):
        """
        Инициализация класса.

        Args:
            list_data: Список чисел.
        """
        if not isinstance(list_data, list):
            raise ValueError("Invalid data type, expected a list.")
        if not list_data:
            raise ValueError("Empty list is not allowed.")
        self._list_data = list_data

    def _get_mean(self):
        """
        Вычисление среднего значения.

        Returns:
            Среднее значение списка.
        """
        numeric_list = []
        for item in self._list_data:
            try:
                numeric_list.append(float(item))
            except ValueError:
                pass
        if not numeric_list:
            return None
        return sum(numeric_list) / len(numeric_list)

    def get_mean(self) -> float:
        """
        Получение среднего значения.

        Returns:
            Среднее значение списка.
        """
        if not self._list_data:
            return None
        return self._get_mean()

    def get_standard_deviation(self) -> float:
        """
        Получение стандартного отклонения списка.

        Returns:
            Значение стандартного отклонения.
        """
        mean = self.get_mean()
        variance = sum((x - mean) ** 2 for x in self._list_data) / len(self._list_data)
        return variance ** 0.5
