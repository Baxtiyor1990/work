from api.hh_api import search_vacancies
from utils.helpers import filter_vacancies, get_top_vacancies, sort_vacancies


def user_interaction():
    # Ввод данных от пользователя
    search_query = input("Введите поисковый запрос: ")
    vacancies_count = int(input("Введите количество вакансий для вывода в топ N: "))

    # Поиск вакансий
    response = search_vacancies(search_query, vacancies_count)

    # Обработка полученных вакансий
    if response.get("items"):
        all_vacancies = response.get("items")

        # Фильтрация вакансий по каким-то критериям (можно настроить под ваш проект)
        filtered_vacancies = filter_vacancies(all_vacancies)

        # Сортировка вакансий
        sorted_vacancies = sort_vacancies(filtered_vacancies)

        # Получение топ N вакансий
        top_vacancies = get_top_vacancies(sorted_vacancies, vacancies_count)

        # Вывод результатов
        print(f"Топ {vacancies_count} вакансий по запросу '{search_query}':")
        for idx, vacancy in enumerate(top_vacancies, start=1):
            print(f"{idx}. {vacancy.get('name')} - {vacancy.get('salary')}")

    else:
        print("По вашему запросу вакансий не найдено.")


# Вызов функции для взаимодействия с пользователем
user_interaction()
