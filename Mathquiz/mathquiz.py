# Quizz
counter = 0

# question 1
student_answer1 = input("Question 1: What is 2 x 3? ")
student_answer1 = int(student_answer1)
corect_answer1 = 2 * 3
if student_answer1 == corect_answer1:
    affirmation = "Congratulations!"
    counter = counter + 1
else:
    affirmation = "Wrong answer!"
print(f"You answered {student_answer1}. The correct answer is {corect_answer1}. {affirmation}")

# question 2
student_answer2 = input("Question 2: What does 10 - 5 make?: ")
student_answer2 = int(student_answer2)
corect_answer2 = 10 - 5
if student_answer2 == corect_answer2:
    affirmation = "Congratulations!"
    counter = counter + 1
else:
    affirmation = "Wrong answer!"
print(f"You answered {student_answer2}. The correct answer is {corect_answer2}. {affirmation}")

# question 3
student_answer3 = input("Question 3: How much is 100 / 2?: ")
student_answer3 = int(student_answer3)
corect_answer3 = int(100 / 2)
if student_answer3 == corect_answer3:
    affirmation = "Congratulations!"
    counter = counter + 1
else:
    affirmation = "Wrong answer!"
print(f"You answered {student_answer3}. The correct answer is {corect_answer3}. {affirmation}")

# question 4
student_answer4 = input("Question 4: How much is 100 x 2?: ")
student_answer4 = int(student_answer4)
corect_answer4 = 100 * 2
if student_answer4 == corect_answer4:
    affirmation = "Congratulations!"
    counter = counter + 1
else:
    affirmation = "Wrong answer!"
print(f"You answered {student_answer4}. The correct answer is {corect_answer4}. {affirmation}")

# Final score
if student_answer1 == corect_answer1 and student_answer2 == corect_answer2 and student_answer3 == corect_answer3 and student_answer4 == corect_answer4:
    print(f"You answered correctly to {counter} questions. You passed the test!")
else:
    print(f"You answered correctly to {counter} questions. Start the test again!")
