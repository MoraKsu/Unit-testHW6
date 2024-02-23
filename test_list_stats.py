"""
Модуль тестирования функциональности класса ListStats.
"""
import unittest

import pytest
from list_stats import ListStats


class TestListStats(unittest.TestCase):
    """
    Тест функциональности класса ListStats.
    """
    def test_list_stats_mean(self):
        """
        Тестирование вычисления среднего значения списка
        """
        test_list = [1, 2, 3, 4, 5]
        stats = ListStats(test_list)
        assert stats.get_mean() == 3.0

    def test_list_stats_mean_empty_list(self):
        """
        Тестирование на выброс ValueError при пустом списке
        """
        with pytest.raises(ValueError):
            ListStats([])

    def test_list_stats_mean_invalid_data_type(self):
        """
        Тестирование на выброс ValueError при неправильном типе данных
        """
        with pytest.raises(ValueError):
            ListStats("not_a_list")

    def test_list_stats_mean_float(self):
        """
        Тестирование вычисления среднего значения списка с дробными числами
        """
        test_list = [1.5, 2.5, 3.5, 4.5, 5.5]
        stats = ListStats(test_list)
        assert stats.get_mean() == 3.5


if __name__ == '__main__':
    unittest.main()
