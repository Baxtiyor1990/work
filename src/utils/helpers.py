def filter_vacancies(vacancies_list, filter_words):
    filtered_vacancies = []
    for vacancy in vacancies_list:
        description_lower = vacancy.description.lower()
        if any(keyword.lower() in description_lower for keyword in filter_words):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies

def get_vacancies_by_salary(vacancies, salary_range):
    if '-' in salary_range:
        min_salary, max_salary = map(int, salary_range.split('-'))
        return [vacancy for vacancy in vacancies if min_salary <= get_salary(vacancy) <= max_salary]
    else:
        # Если диапазон не указан, просто вернем все вакансии
        return vacancies


def sort_vacancies(vacancies_list):
    sorted_vacancies = sorted(vacancies_list, key=lambda x: x.salary, reverse=True)
    return sorted_vacancies

def get_top_vacancies(vacancies_list, top_n):
    return vacancies_list[:top_n]

def print_vacancies(vacancies_list):
    for vacancy in vacancies_list:
        print(vacancy)
