import unittest

import test_list_comparator
import test_list_stats
import test_main


if __name__ == '__main__':
    # Создаем TestSuite
    test_suite = unittest.TestSuite()

    # Добавляем тесты из каждого модуля в TestSuite
    test_suite.addTest(unittest.TestLoader().loadTestsFromModule(test_list_comparator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromModule(test_list_stats))
    test_suite.addTest(unittest.TestLoader().loadTestsFromModule(test_main))

    # Запускаем тесты и выводим результаты
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
