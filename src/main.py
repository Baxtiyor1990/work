from api.hh_api import HeadHunterAPI
from models.vacancy import Vacancy, JSONSaver
from utils.helpers import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies

def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (пример: 100000-150000): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)

    print("Ответ API:", hh_vacancies)  # Добавим вывод для отладки

    if hh_vacancies and 'items' in hh_vacancies:
        vacancies_list = [Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy.get('salary', {}).get('from', 'Зарплата не указана'), vacancy.get('description', 'Описание отсутствует')) for vacancy in hh_vacancies['items']]
        filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
        ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
        sorted_vacancies = sort_vacancies(ranged_vacancies)
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print_vacancies(top_vacancies)
    else:
        print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")


if __name__ == "__main__":
    user_interaction()
