from module import *

class Level1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backBtn = tk.PhotoImage(file='factory/backButton.png')
        self.goImage = tk.PhotoImage(file='factory/go1.png')
        self.nogoImage = tk.PhotoImage(file='factory/nogo1.png')
        self.exitImage = tk.PhotoImage(file='factory/exit1.png')

        # Level1 Canvas
        self.canvas = tk.Canvas(self, width=1600, height=1200)
        self.canvas.pack()

        # Level1 Title
        self.canvas.create_text(720, 60, text="Level1", font=("Helvetica", 70, 'bold'))

        # Level1 Map
        self.gameMap = [
            [0, 0, 1, 3],
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
        ]

        for r in range(4):
            for c in range(4):
                if self.gameMap[r][c] == 1:
                    self.canvas.create_image(c * 170 + 470, r * 170 + 200, image=self.goImage)
                    # self.canvas.create_rectangle(c*50, r*50, c*50+50, r*50+50, fill='green' )
                elif self.gameMap[r][c] == 0:
                    self.canvas.create_image(c * 170 + 470, r * 170 + 200, image=self.nogoImage)
                elif self.gameMap[r][c] == 3:
                    self.canvas.create_image(c * 170 + 470, r * 170 + 200, image=self.exitImage)

        # Previous Button
        self.backBtn = tk.PhotoImage(file='factory/exitButton2.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                                  command=lambda: controller.show_frame("StartPage"))
        self.canvas.create_window(1375, 60, window=backButton)