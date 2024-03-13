import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from источник.main import user_interaction

class TestMainFunction(unittest.TestCase):
    @patch('источник.API.hh_api.HeadHunterAPI.get_vacancies', return_value={'items': [
        {'name': 'Python Developer', 'alternate_url': 'https://example.com', 'salary': {'from': 120000}, 'description': 'Description 1'},
        {'name': 'Java Developer', 'alternate_url': 'https://example.com', 'salary': {'from': 130000}, 'description': 'Description 2'},
    ]})
    @patch('builtins.input', side_effect=['Python Developer', '5', 'python', '100000-150000'])
    def test_user_interaction(self, mock_input, mock_api):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_interaction()
            output = mock_stdout.getvalue().strip()

        self.assertIn("Python Developer", output)
        self.assertIn("Зарплата: 120000", output)
        self.assertIn("Ссылка: https://example.com", output)
        self.assertIn("Описание: Description 1", output)

if __name__ == '__main__':
    unittest.main()
