class QuizBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0 
    def next_question(self):
        score = 0
        for element in self.question_list: 
            self.question_number += 1 
            for question in element.keys():
                answer = input(f"Q{self.question_number}. {question}? (True/False) ")
                if answer == element[question]:
                    score += 1
                elif answer != element[question]:
                    break


        if score == len(self.question_list):
            print(f"You finished the game with score of {score}! you are a master of this game")
                        
        else:
            print(f"Your score is {score}! Study more")
                    
    
