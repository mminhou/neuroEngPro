from module import *

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Intro Wallpaper
        self.canvas = tk.Canvas(self, width=1600, height=1200)
        # self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.pack(fill="both", expand=True)
        self.sequence2 = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(
            Image.open(r'factory/startWall.gif')
        )]
        # self.image = self.canvas.create_image(0, 0, image=self.sequence[0], anchor="nw")
        self.image2 = self.canvas.create_image(720, 305, image=self.sequence2[0])
        self.animating2 = True
        self.animate2(0)

        # Level2 Button
        self.level2Btn = tk.PhotoImage(file='factory/level2.png')
        level2Button = tk.Button(self, image=self.level2Btn, borderwidth=0, highlightthickness=0,
                                command=lambda: controller.show_frame("Level1Page"))
        self.canvas.create_window(310, 290, window=level2Button)

        # Level3 Button
        self.level3Btn = tk.PhotoImage(file='factory/level3.png')
        level3Button = tk.Button(self, image=self.level3Btn, borderwidth=0, highlightthickness=0,
                                   command=lambda: controller.show_frame("Level2Page"))
        self.canvas.create_window(710, 290, window=level3Button)

        # Level1 Button
        self.level1Btn = tk.PhotoImage(file='factory/level1.png')
        level1Button = tk.Button(self, image=self.level1Btn, borderwidth=0, highlightthickness=0,
                                   command=lambda: controller.show_frame("Level3Page"))
        self.canvas.create_window(1110, 290, window=level1Button)

        # Exit Button
        self.backBtn = tk.PhotoImage(file='factory/exitButton.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(1375, 60, window=backButton)

        # label = tk.Label(self, text="This is Start Page", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        # button2 = tk.Button(self, text="Level1",
        #                    command=lambda: controller.show_frame("Level1Page"))
        # button2.pack()
        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("IntroPage"))
        # button.pack()
        # button2.pack()

    def animate2(self, counter):
        self.canvas.itemconfig(self.image2, image=self.sequence2[counter])
        if not self.animating2:
            return
        self.after(100, lambda: self.animate2((counter+1) % len(self.sequence2)))
