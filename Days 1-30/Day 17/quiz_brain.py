class QuizBrain:

    def __init__(self , q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        while self.question_number != len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            if input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower() == current_question.answer.lower():
                self.score += 1
                print(f"You got it right! \nThe correct answer was: {current_question.answer}. \nYour current score is {self.score}/{self.question_number}.")
            else:
                print(f"That's wrong. \nThe correct answer was: {current_question.answer}. \nYour current score is {self.score}/{self.question_number}.\n\n")
        print(f"Final Score: {self.score}/{self.question_number}.")