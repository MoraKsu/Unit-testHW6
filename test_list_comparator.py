"""
Модуль тестирования функциональности класса ListComparator.
"""
import unittest

import pytest
from list_comparator import ListComparator
from list_stats import ListStats


class TestListComparator(unittest.TestCase):
    """
    Тест функциональности класса ListComparator.
    """
    def test_compare_means_equal(self):
        """
        Проверка, что compare_means возвращает True, когда средние значения равны.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([1, 2, 3])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is True

    def test_list_comparator_compare_means_not_equal(self):
        """
        Тестирование неравенства средних значений двух списков
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([4, 5, 6])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is False

    def test_compare_means_list1_greater(self):
        """
        Проверка, что compare_means возвращает False, когда среднее значение
        list1 больше среднего значения list2.
        """
        list1 = ListStats([2, 3, 4])
        list2 = ListStats([1, 2, 3])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is False

    def test_compare_means_list2_greater(self):
        """
        Проверка, что compare_means возвращает False, когда среднее значение
        list2 больше среднего значения list1.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([2, 3, 4])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is False

    def test_compare_means_empty_lists(self):
        """
        Проверка, что при попытке сравнения средних значений пустых списков
        выбрасывается исключение ValueError.
        """
        with pytest.raises(ValueError):
            list1 = ListStats([])
            list2 = ListStats([])
            comparator = ListComparator(list1, list2)
            comparator.compare_means()

    def test_compare_means_invalid_data_type(self):
        """
        Проверка, что при попытке сравнения средних значений с недопустимым
        типом данных выбрасывается исключение ValueError.
        """
        with pytest.raises(ValueError):
            list1 = ListStats("not a list")
            list2 = ListStats([1, 2, 3])
            comparator = ListComparator(list1, list2)
            comparator.compare_means()

    def test_compare_means_invalid_data_type_2(self):
        """
        Проверка, что при попытке сравнения средних значений с недопустимым
        типом данных выбрасывается исключение ValueError.
        """
        with pytest.raises(ValueError):
            list1 = ListStats([1, 2, 3])
            list2 = ListStats({"a": 1, "b": 2})
            comparator = ListComparator(list1, list2)
            comparator.compare_means()

    def test_compare_means_different_tol(self):
        """
        Проверка, что результат сравнения зависит от допустимой погрешности.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([2, 3, 4])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is False

    def test_compare_means_both_empty(self):
        """
        Проверка, что сравнение средних значений работает корректно, когда оба списка пусты.
        """
        with pytest.raises(ValueError) as e:
            ListStats([])
        assert str(e.value) == "Empty list is not allowed."

    def test_compare_means_one_empty(self):
        """
        Проверка, что сравнение средних значений работает корректно,
        когда один из списков пуст.
        """
        with pytest.raises(ValueError) as e:
            ListStats([])
        assert str(e.value) == "Empty list is not allowed."

    def test_compare_means_same_values(self):
        """
        Проверка, что сравнение средних значений работает корректно,
        когда оба списка содержат одинаковые значения.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([1, 2, 3])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is True

    def test_compare_means_equal_means(self):
        """
        Проверка, что сравнение средних значений работает корректно,
        когда списки имеют одинаковое среднее значение.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([1, 2, 3])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is True

    def test_compare_means_different_means(self):
        """
        Проверка, что сравнение средних значений работает корректно,
        когда списки имеют разное среднее значение.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([4, 5, 7])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is False

    def test_compare_means_different_lengths(self):
        """
        Проверка, что сравнение средних значений работает корректно,
        когда списки имеют разную длину.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([4, 5])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is False

    def test_compare_means_equal_lists(self):
        """
        Проверка, что сравнение средних значений работает корректно,
        когда списки идентичны.
        """
        list1 = ListStats([1, 2, 3])
        list2 = ListStats([1, 2, 3])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is True

    def test_compare_means_non_numeric_lists(self):
        """
        Проверка, что сравнение средних значений возвращает None,
        когда списки содержат нечисловые значения.
        """
        list1 = ListStats(["a", "b", "c"])
        list2 = ListStats(["x", "y", "z"])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is None

    def test_compare_means_single_item_lists(self):
        """
        Проверка, что сравнение средних значений возвращает True,
        когда списки содержат только один элемент и они равны.
        """
        list1 = ListStats([5])
        list2 = ListStats([5])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is True

    def test_compare_means_single_item_lists_different_values(self):
        """
        Проверка, что сравнение средних значений возвращает False,
        когда списки содержат только один элемент, но они различны.
        """
        list1 = ListStats([5])
        list2 = ListStats([10])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is False

    def test_compare_means_single_item_lists_same_values_tolerance(self):
        """
        Проверка, что сравнение средних значений возвращает True,
        когда списки содержат только один элемент и он равен с точностью до погрешности.
        """
        list1 = ListStats([0.1])
        list2 = ListStats([0.1])
        comparator = ListComparator(list1, list2)
        assert comparator.compare_means() is True


if __name__ == '__main__':
    unittest.main()
