from question_model import Question
#from data import question_data
from data2 import question_data
from quiz_brain import QuizBrain
import requests


question_bank = []

def get_new_questions():
    request = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
    question_data = request.json()['results']
    with open('data2.py', 'w') as file:
        file.write('question_data = ' +  str(question_data))


get_new_questions()

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
