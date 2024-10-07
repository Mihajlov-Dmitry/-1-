import random


class Play:
    def __init__(self):
        self.condition = "play"
        self.console_interface = Interface()
        self.random_word = self.get_random_word()
        self.attempts = set()
        self.fail_counter = 0
        self.counter = 0

    def start(self):
        self.console_interface.setting_game()
        self.console_interface.play(condition=self.condition)

    def print_human(self):
        # доступно 9 ошибок
        self.output_list = [
            """
   ==============
   ||       |
   ||       |       
   ||      
   ||    
   ||   
   ||      
   ||      
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    
   ||   
   ||      
   ||     
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||     |   |
   ||     |   | 
   ||      ---
   ||     
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |
   ||   / |   | 
   ||      ---
   ||     
   ||     
   ||  
___||____________    
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      
   ||     
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      / 
   ||      
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      / 
   ||     /   
   ||  
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      / \\
   ||     /   
   ||    
___||____________
            """,
            """
   ==============
   ||       |
   ||       |       
   ||      ( )
   ||    /|   |\\
   ||   / |   | \\
   ||      ---
   ||      / \\
   ||     /   \\
   ||    
___||____________
            """
        ]

    def get_random_word(self) -> str:
        """
        Возвращает рандомное слово
        :return:
        """
        with open("words.txt", "r") as words_file:
            words_list = words_file.readlines()
        words_file.close()
        return random.choice(words_list)

    def checking_attempt(self, answer) -> int:
        """
        Проверяет введенный пользователем ответ
        :param answer:
        :return:
        """
        if answer in self.attempts:  # если ответ уже получался ранее
            return 2
        else:
            self.counter += 1
            self.attempts.add(answer)
            if answer in self.random_word:  # если ответ верный
                return 1
            else:  # если ответ неверный
                self.fail_counter += 1
                return 0


if __name__ == "__main__":
    play = Play()
    play.start()
