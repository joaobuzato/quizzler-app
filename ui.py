from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.question_canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_canvas.create_text(150, 125, width=280, text="TEXTO TESTE", font=FONT)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_canvas.config(bg='white')
        self.question_canvas.itemconfig(self.question_text, text=q_text)

    def give_feedback(self, is_right):

        if is_right:
            self.question_canvas.config(bg='green')
        else:
            self.question_canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
