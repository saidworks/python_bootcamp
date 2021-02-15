class Question:
    def __init__(self,text=None,answer=None):
        self.text = text
        self.answer = answer 
    def model(self,question_data):
        self.question_data = question_data
        bank = []
        for entry in question_data:
            bank.append({entry["text"]:entry["answer"]})
        return bank

# new_q = Question("who's the supreme leader?","Said")
# print(new_q.q_text,new_q.q_answer)