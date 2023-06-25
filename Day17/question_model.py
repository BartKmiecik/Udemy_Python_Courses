class QuestionModel:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

    def validate(self, guess: str):
        if self.answer == guess:
            return True
        return False