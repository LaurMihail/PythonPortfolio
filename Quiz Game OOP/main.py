from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def print_intro():
    name = input("Welcome! What's your name? ")
    print(f"Hello, {name}! Let's start the quiz.")
    return name


def print_outro(name, score, total_questions):
    print(f"Goodbye, {name}! You've completed the quiz.")
    print(f"Your final score was: {score}/{total_questions}")


player_name = print_intro()


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# if __name__ == '__main__':
#     print_hi('PyCharm')


print_outro(name=player_name, score=quiz.score, total_questions=quiz.question_number)
