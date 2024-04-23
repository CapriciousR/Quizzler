from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(height=350, width=400, bg="white")
        self.qntext = self.canvas.create_text(200, 175, text="Question text goes here", width = 360, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)
        
        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        
        self.true_button = Button(image=right_img, highlightthickness=0, command=self.right_button_clicked)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=wrong_img, highlightthickness=0, command=self.wrong_button_clicked)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg= "white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.qntext, text=q_text)
        else:
            self.canvas.itemconfig(self.qntext, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right: bool):
        print(is_right)
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.update()
            print("Canvas should be green")
        else:
            self.canvas.config(bg="red")
            self.canvas.update()
            print("Canvas should be red")
         
        self.window.after(1000, self.get_next_question())


           