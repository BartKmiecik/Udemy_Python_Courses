from data import question_data
from question_model import QuestionModel
import random

class QuizBrain:
    def __init__(self):
        self.all_questions = []
        for i in question_data:
            text = i['text']
            answer = i['answer']
            question = QuestionModel(text, answer)
            self.all_questions.append(question)
        random.shuffle(self.all_questions)
        self.counter = -1

    def get_next(self):
        self.counter += 1
        return self.all_questions[self.counter]

