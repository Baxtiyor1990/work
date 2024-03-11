import unittest
from unittest.mock import patch
from models.vacancy import JSONSaver, Vacancy

class TestJSONSaverClass(unittest.TestCase):
    @patch('builtins.open', create=True)
    def test_add_vacancy(self, mock_open):
        vacancy = Vacancy("Python Developer", "example.com", "100000-150000", "Experience: 3 years")
        json_saver = JSONSaver()

        json_saver.add_vacancy(vacancy)

        # Проверка, что метод open был вызван с ожидаемыми параметрами
        mock_open.assert_called_once_with('vacancies.json', 'a')

if __name__ == '__main__':
    unittest.main()
