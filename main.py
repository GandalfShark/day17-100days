from question_model import Question
from data import question_data2
from quiz_brain import QuizBrain
# Day 17 of 100 days of python by Dr.Angela Yu

print("""
^^^^^^^^^^^^^^^^^^^
TRUE or FALSE game
^^^^^^^^^^^^^^^^^^^
""")

question_bank = []
for q in question_data2:
    question_bank.append(Question(q['question'], q['correct_answer']))
    # create an object for each of these questions in the data bank

# for i in range(12):
#     print(question_bank[i].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print('You completed the quiz game!')
print(f'Your final score was: {quiz.score} out of {len(question_bank)}')