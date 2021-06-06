from module import *
import math

class FailPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Wallpaper
        self.canvas = tk.Canvas(self, width=1600, height=1200, bg='white')
        self.canvas.pack(fill="both", expand=True)

        # Title
        self.canvas.create_text(700, 200, text="Time's Up", font=("Helvetica", 80, 'bold'), fill="Black")

        # Graph Image
        # self.image = self.canvas.create_image(740, 500, image=self.graphWall)

        # Previous Button
        backButton = tk.Button(self, text="go home",
                               font=("Helvetica", 80, 'bold'),
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(700, 300, window=backButton)

