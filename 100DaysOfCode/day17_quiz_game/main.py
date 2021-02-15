from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
new_q = Question()
question_bank=new_q.model(question_data)
quiz = QuizBrain(question_bank)
quiz.next_question()
