from module import *

class Level2Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backBtn = tk.PhotoImage(file='factory/image/backButton.png')
        self.goImage = tk.PhotoImage(file='factory/image/go2.png')
        self.nogoImage = tk.PhotoImage(file='factory/image/nogo2.png')
        self.exitImage = tk.PhotoImage(file='factory/image/exit2.png')

        # Level2 Canvas
        self.canvas = tk.Canvas(self, width=1600, height=1200)
        self.canvas.pack()

        # Level2 Title
        self.canvas.create_text(720, 60, text="Level2", font=("Helvetica", 70, 'bold'))

        # Level2 Map
        self.gameMap = [
            [0, 0, 0, 0, 0, 0, 1, 3],
            [0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]

        for r in range(8):
            for c in range(8):
                if self.gameMap[r][c] == 1:
                    self.canvas.create_image(c * 85 + 420, r * 85 + 160, image=self.goImage)
                elif self.gameMap[r][c] == 0:
                    self.canvas.create_image(c * 85 + 420, r * 85 + 160, image=self.nogoImage)
                elif self.gameMap[r][c] == 3:
                    self.canvas.create_image(c * 85 + 420, r * 85 + 160, image=self.exitImage)

        # Previous Button
        self.backBtn = tk.PhotoImage(file='factory/image/exitButton2.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                                borderwidth=0, highlightthickness=0,
                                command=lambda: controller.show_frame("StartPage"))
        self.canvas.create_window(1375, 60, window=backButton)
