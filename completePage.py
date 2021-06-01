from module import *

class CompletePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        # Wallpaper
        self.canvas = tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack(fill="both", expand=True)

        # Graph Title
        self.canvas.create_text(350, 100, text="Clear!", font=("Helvetica", 70, 'bold'))

        # Graph Image
        # self.image = self.canvas.create_image(740, 500, image=self.graphWall)

        # Previous Button
        self.backBtn = tk.PhotoImage(file='factory/image/exitButton.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(1375, 60, window=backButton)

