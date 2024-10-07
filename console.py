from game import Game
from data.text import text
import string


class Interface(Game):
    def __init__(self) -> None:
        super().__init__()
        self.complexity = "easy"
        self.language = "rus"

    def setting_game(self) -> None:
        """
        Настройка игры (сложность, язык)
        :return: None
        """
        self.complexity = input(text["complexity_selection"])
        self.language = input(text["language_selection"])

    def play(self) -> None:
        """

        :param condition:
        :return:
        """
        print("start play")

        while self.condition != "finish":
            answer_char = input(text["get_answer"]).strip().lower()  # получить новую букву

            while answer_char not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':  # проверка корректности ввода
                print(text["error"])
                answer_char = input(text["get_answer"])

            match self.checking_attempt(answer_char):  # проверка верности ответа
                case 2:
                    print(text["error_repeating_character"])
                case 1:
                    print(text["correct_answer"])
                case 0:
                    print(text["incorrect_answer"])

            if self.counter_incorrect_answers == self.max_incorrect_answer[self.complexity]:
                self.condition = 'lose'
            elif self.counter_correct_answers == len(self.random_word):
                self.condition = 'win'

        if self.condition == "lose":
            print(text["lose"])
        elif self.condition == "win":
            print(text["win"])
