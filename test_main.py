"""
Модуль тестирования главной функции программы.
"""
import unittest
from io import StringIO
from unittest.mock import patch
import main


class TestMain(unittest.TestCase):
    """
    Тест главной функции программы.
    """
    def test_main_input(self):
        """
        Тестирование ввода пользовательских данных
        """
        user_input = "1,2,3\n4,5,6\n"
        expected_output = "Неверный формат данных. Пожалуйста, введите числовые значения.\n"
        with patch('builtins.input', side_effect=user_input), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            main.main()
            assert fake_out.getvalue() == expected_output


    def test_main_invalid_input(self):
        """
        Тестирование ввода неправильных данных пользователем
        """
        user_input = "a,b,c\nx,y,z\n"
        expected_output = "Неверный формат данных. Пожалуйста, введите числовые значения.\n"
        with patch('builtins.input', side_effect=user_input), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            main.main()
            assert fake_out.getvalue() == expected_output


if __name__ == '__main__':
    unittest.main()
