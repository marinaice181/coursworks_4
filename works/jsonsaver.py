from works.vacancy import Vacancies
from works.abc import JSONABCSaver


class JSONSaver(Vacancies, JSONABCSaver):
    """
    Файл запись и чтение json
    """

    def file_writer(self):
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            pass

    def file_reader(self):
        with open('vacancies.json', 'r', encoding='UTF-8') as file:
            pass