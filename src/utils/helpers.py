import re

def get_salary(vacancy):
    salary = vacancy.salary

    if '-' in salary:
        min_salary, max_salary = map(int, re.findall(r'\d+', salary))
        return (min_salary + max_salary) / 2
    elif salary.isdigit():
        return int(salary)
    else:
        return 0

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
        return vacancies

def sort_vacancies(vacancies_list):
    sorted_vacancies = sorted(vacancies_list, key=lambda x: get_salary(x), reverse=True)
    return sorted_vacancies

def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]

def print_vacancies(vacancies_list):
    for vacancy in vacancies_list:
        print(vacancy)
