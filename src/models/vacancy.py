import json

class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

        # Валидация данных
        if not isinstance(self.salary, (str, int, float)):
            self.salary = "Зарплата не указана"

    def __str__(self):
        return f"{self.title}\nЗарплата: {self.salary}\nСсылка: {self.link}\nОписание: {self.description}\n"

    def __lt__(self, other):
        return self.salary < other.salary

class AbstractVacancySaver:
    def add_vacancy(self, vacancy):
        pass

    def delete_vacancy(self, vacancy):
        pass

    def get_vacancies_by_criteria(self, criteria):
        pass

class JSONSaver(AbstractVacancySaver):
    def __init__(self, file_path="vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'a') as file:
            json.dump(vacancy.__dict__, file)
            file.write('\n')

    def delete_vacancy(self, vacancy):
        # Заглушка для удаления вакансии из файла
        pass

    def get_vacancies_by_criteria(self, criteria):
        # Заглушка для получения вакансий из файла по критериям
        pass
