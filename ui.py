from tkinter import *
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", font=FONT, bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.question_canvas = Canvas(width=300, height=250)
        self.question_canvas.create_text(150,125, text="TEXTO TESTE", font=FONT)
        self.question_canvas.grid(column=0, row=1, columnspan=2, padx=20)
        self.window.mainloop()
