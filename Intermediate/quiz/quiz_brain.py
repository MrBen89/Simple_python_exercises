class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number].text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question} (True/False)?: ")
        self.check_answer(user_answer, self.questions_list[self.question_number-1].answer)


    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Well done, that's right!")
            self.score += 1
        else:
            print("That's wrong, bad luck!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
