from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from quiz_brain import QuizBrain_hard

"""
Satisfies SOB 33
Write code that makes use of a library or external module to carry out specialized tasks. Describe how the interpreter/compiler 'imports'
This  file uses "import" statement to access the codes from different modules(files) in the library(folder) "quiz game".
Satisfies sob 35
{Write and use your own library or class.
A library must include at least two parametric functions; a class must include appropriate properties and methods.}
"""

#question bank is a list of randomly generated question
question_bank = []

def get_questions():
  """adds the quiz questions to the question bank(list of questions)"""
  for i in question_data:
      question_text = i["question"]
      question_answer = i["correct_answer"]
      question = Question(question_text,question_answer)
      question_bank.append(question)


def start_quiz(quiz_length,difficulty):
  """gets the list of questions
  starts the quiz and determines how it goes depending on the length of the quiz and difficulty
   determined by the user
   satisfies SOB 32(Create functions that use parameters and provide results in appropriate types) """
  get_questions()
  if difficulty == 'e':
    """you have unlimited lives"""
    tries = quiz_length
    quiz = QuizBrain(question_bank)
  elif difficulty == 'd':
    """the number of lives you have is 30% of the length of the quiz"""
    tries = round(0.3 * quiz_length)
    print(f"You have {tries} lives")
    quiz = QuizBrain_hard(question_bank,tries)
    
  while quiz.still_has_questions(quiz_length) and tries>0:
    """while loop runs as far as you have lives left and there are still questions left in the quiz"""
    quiz.next_question()
    

  print(f"You have completed the quiz!\nYour final score is {quiz.score}/{quiz.question_number}")



quiz_length = int(input("Meeda's Quiz game:)\nThere are 50 trivia questions\nHow many questions would you like to answer?\nYou have a minimum of 5 questions and a maximum of 50"))

difficulty = input("What level of difficulty do you want?\ne-Easy\nd-Difficult\n")



start_quiz(quiz_length,difficulty)