import unittest
from src.models.vacancy import Vacancy
from src.utils.helpers import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, get_salary

class TestHelpersFunctions(unittest.TestCase):
    def setUp(self):
        self.vacancies_list = [
            Vacancy("Python Developer", "example1.com", "100000", "Experience: 3 years"),
            Vacancy("Java Developer", "example2.com", "120000", "Experience: 5 years"),
            Vacancy("Frontend Developer", "example3.com", "80000-100000", "React, Angular")
        ]

    def test_filter_vacancies(self):
        filtered_vacancies = filter_vacancies(self.vacancies_list, ['Python', 'React'])

        self.assertEqual(len(filtered_vacancies), 2)
        self.assertIn(self.vacancies_list[0], filtered_vacancies)
        self.assertIn(self.vacancies_list[2], filtered_vacancies)

    def test_get_vacancies_by_salary(self):
        ranged_vacancies = get_vacancies_by_salary(self.vacancies_list, '90000-120000')

        self.assertEqual(len(ranged_vacancies), 2)
        self.assertIn(self.vacancies_list[0], ranged_vacancies)
        self.assertIn(self.vacancies_list[1], ranged_vacancies)

    def test_sort_vacancies(self):
        sorted_vacancies = sort_vacancies(self.vacancies_list)

        self.assertEqual(sorted_vacancies, [self.vacancies_list[1], self.vacancies_list[0], self.vacancies_list[2]])

    def test_get_top_vacancies(self):
        top_vacancies = get_top_vacancies(self.vacancies_list, 2)

        self.assertEqual(top_vacancies, [self.vacancies_list[1], self.vacancies_list[0]])

if __name__ == '__main__':
    unittest.main()
