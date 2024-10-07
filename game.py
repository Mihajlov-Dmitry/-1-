import random
from data.resources import humans_list


def get_random_word() -> str:
    """
    Возвращает рандомное слово
    :return:
    """
    with open(r"data\words.txt", "r") as words_file:
        words_list = words_file.readlines()
    words_file.close()
    return random.choice(words_list)


class Game:
    def __init__(self) -> None:
        self.condition = "play"
        self.complexity = "easy"
        self.random_word = get_random_word()
        self.humans_list = humans_list
        self.old_answers = set()
        self.counter_correct_answers = 0
        self.counter_incorrect_answers = 0
        self.max_incorrect_answer = {
            "easy": 9,
            "medium": 7,
            "hard": 5,
        }

    def checking_attempt(self, answer: str) -> int:
        """
        Проверяет введенный пользователем ответ
        :param answer:
        :return:
        """
        if answer in self.old_answers:
            return 2
        else:
            self.old_answers.add(answer)
            if answer in self.random_word:
                self.counter_correct_answers += 1
                return 1
            else:
                self.counter_incorrect_answers += 1
                return 0

