from quiz_brain import QuizBrain

brain = QuizBrain()
score = -1
while True:
    score += 1
    question = brain.get_next()
    answer = input(question.question)
    if not question.validate(answer):
        break

print(f'Thanks for playing you\'r score is {score}')