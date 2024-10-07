from text import text
import string


def main():
    max_fail_count = {
        "easy": 9,
        "medium": 7,
        "hard": 5,
    }


class Interface:
    def __init__(self):
        self.complexity = None
        self.language = "rus"

    def setting_game(self) -> None:
        """
        Настройка игры (сложность, язык)
        :return: None
        """
        self.complexity = input(text["complexity_selection"])
        self.language = input(text["language_selection"])

    def play(self, condition):
        """

        :param condition:
        :return:
        """
        while condition != "finish":
            answer_char = input(text["get_answer"])  # получить новую букву

            while answer_char not in string.ascii_lowercase:  # проверка корректности ввода
                print(text["error"])
                answer_char = input(text["get_answer"])

            match checking_attempt(answer_char):  # проверка верности ответа
                case 2:
                    print(text["error_repeating_character"])
                case 1:
                    print(text["correct_answer"])
                case 0:
                    print(text["incorrect_answer"])
