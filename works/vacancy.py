class Vacancy:
    """
    Вакансии
    """

    def __init__(self, vacancy_title, town, salary_from, salary_to, employment, url):
        self.vacancy_title: str = vacancy_title
        self.town: str = town
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.employment: str = employment
        self.url: str = url

    def __str__(self):
        return f'название вакансии: {self.vacancy_title}\n' \
               f'город: {self.town}\n' \
               f'зарплата от: {self.salary_from}\n' \
               f'зарплата до: {self.salary_to}\n' \
               f'Занятость: {self.employment}\n' \
               f'ссылка на вакансию: {self.url}\n'

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from > other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError()
        return self.salary_from >= other.salary_from

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        pass

    @staticmethod
    def from_dict(vacancy_dict):
        """
        Возвращает вакансию в виде списка
        """
        pass



class Vacancies:
    """
    Обработка списка вакансий
    """

    def __init__(self):
        self.__all_vacancies = []
