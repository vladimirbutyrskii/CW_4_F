from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, keyword):

        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': 100}


    def load_vacancies(self):
        vacancies = []

        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            vacancies.extend(vacancies)
            self.params['page'] += 1

        return vacancies

# if __name__ == "__main__":
#     hh = HH("курьер")
#     res = hh.load_vacancies()
#     for i in res:
#         print(i["id"], i["salary"])
    #print(res)