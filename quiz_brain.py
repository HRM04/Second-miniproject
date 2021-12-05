import random #satiesfies SOB 33 by importing an external module


"""
 Satisfies SOB 34
 {Write code that utilizes classes/objects/methods in an appropriate scenario. 
 Instantiate an object and modify its state using methods.}
 These classes take care of the technicality of the game.
 It determines what the quiz does and when it does it.
 Satisfies SOB 35
 {Write and use your own library or class. 
 A library must include at least two parametric functions; a class must include appropriate properties and methods.}
 """
class QuizBrain():

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self,quiz_length):
      """return true if the quiz still has questions left(based on the quiz length chosen""" 
      return self.question_number < quiz_length
        

    def next_question(self):
      """gives you the next question from a list of ramdomly generated questions gotten from the 'data' file """
      current_question = random.choice(self.question_list)
      self.question_number += 1
      user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)\n")
      self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
      """checks the answer provided by th euser against the correct answer 
      and determines the score of the user based on the current question"""
      if user_answer.lower() == correct_answer.lower():
        print("You got it right")
        self.score += 1
      else:
        print("You got it wrong")
      print(f"The correct answer is {correct_answer}")
      print(f"Your current score is: {self.score}/{self.question_number}\n")




class QuizBrain_hard(QuizBrain):
  def __init__(self, q_list, tries):
    super().__init__(q_list)
    self.number_of_tries = tries

  def number_of_tries_left(self, user_answer, correct_answer):
    """returns the number of lives left when difficulty of the quiz is diificult"""
    if user_answer.lower() != correct_answer.lower():
      self.number_of_tries -= 1
    print(f"You have {self.number_of_tries} lives left")
    return self.number_of_tries

  def next_question(self):
    """returns the next question if the number of lives left is not zero"""
    current_question = random.choice(self.question_list)
    self.question_number += 1
    user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False) ")
    self.check_answer(user_answer, current_question.answer)
    self.number_of_tries_left(user_answer, current_question.answer)
  

  def still_has_questions(self,quiz_length):
    """return true if the quiz still has questions and the number of lives left is not zero """
    return self.question_number < quiz_length  and self.number_of_tries>0


        
    



    

