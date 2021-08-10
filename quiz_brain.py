class QuizBrain:
    def __init__(self, question_list): 
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self): 
        current_question = self.question_list[self.question_number].question
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number}: {current_question} (True/False)").lower() 
        self.check_answer(users_answer, correct_answer)
        self.show_score() 

    def more_question(self):
        if self.question_number < len(self.question_list): 
            return True
        else:
            return False
    
    def show_score(self):
        print(f"You got {self.score}/{len(self.question_list)}")
        #print in a new line 
        print("\n")
        if self.question_number == len(self.question_list):
            print("The Quiz has ended!")
    
    def check_answer(self, users_answer, correct_answer):
        if users_answer.lower() == correct_answer.lower(): 
            self.score += 1
            print(f"You got it right!") 
            
        else:
            print(f"Oops! You got it wrong.")
        print(f"The correct answer was {correct_answer}") 
    

