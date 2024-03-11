import unittest
from unittest.mock import patch
from io import StringIO
from src.main import user_interaction


class TestMainFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['Python Developer', '5', 'python', '100000-150000'])
    def test_user_interaction(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            user_interaction()
            output = mock_stdout.getvalue().strip()

        self.assertIn("Python Developer", output)
        self.assertIn("Зарплата: ", output)
        self.assertIn("Ссылка: ", output)
        self.assertIn("Описание: ", output)


if __name__ == '__main__':
    unittest.main()
