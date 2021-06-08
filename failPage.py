from module import *

class FailPage(tk.Frame):
    ''' FailPage '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ''' Fail Wallpaper'''
        self.canvas = tk.Canvas(self, width=1600, height=1200, bg='white')
        self.canvas.pack(fill="both", expand=True)

        ''' Fail Title '''
        self.canvas.create_text(700, 200, text="Time's Up", font=("Helvetica", 60, 'bold'), fill="red")

        ''' Go Home(IntroPage) Button '''
        homeButton = tk.Button(self, text="Go home",
                               font=("Helvetica", 50, 'bold'),
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(700, 400, window=homeButton)

