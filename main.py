from typing import Any, List

from src.parser import HH
from src.json_worker import WorkWithJson
from src.user_interactive import UserInteractive
from src.vacancy import Vacancy

if __name__ == "__main__":

    print("Hello, user")
    user_name = input("Как ваше имя?  ")
    user = UserInteractive(user_name)

    keyword = input("Введите запрос: ")

    for vacancy in user.get_vacancies_list(keyword):
        vac = Vacancy.new_vacancy(vacancy)
        user.vacancies_list.append(vac)
        # print(vac)
        # print()

    """print(user_vac_list[0] < user_vac_list[1])
    print(user_vac_list[1] < user_vac_list[2])
    print(user_vac_list[2] < user_vac_list[3])"""

    for vacancy in user.get_top_n_for_salary():
        print(vacancy)