class QuizBrain:
  def __init__(self, q_list):
    self.question_no = 0
    self.question_list = q_list
    self.score = 0
  def still_has_question(self):
    return self.question_no < len(self.question_list)

  def next_question(self):
    current_question = self.question_list[self.question_no]
    self.question_no += 1
    u_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
    self.check_answer(u_answer, current_question.answer)

  def check_answer(self, user_answer, r_answer):
    if user_answer == r_answer.lower():
      print(f"You got it right!")
      self.score += 1
    else:
      print("You got it wrong!")
    print(f"The correct answer is: {r_answer}")
    print(f"Your score: {self.score}/{self.question_no}")