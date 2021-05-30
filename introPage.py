from module import *

class IntroPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Intro Wallpaper
        # self.canvas = tk.Canvas(self, width=1600, height=1200)
        self.canvas = tk.Canvas(self, width=1200, height=1000)
        # self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.canvas.pack(fill="both", expand=True)
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(
            Image.open(r'factory/image/original2.gif')
        )]
        self.image = self.canvas.create_image(720, 400, image=self.sequence[0])
        # self.image = self.canvas.create_image(-180, -200, image=self.sequence[0], anchor="nw")
        self.animating = True
        self.animate(0)

        # Intro Title
        # self.canvas.create_text(700, 200, text="Neuro Engineering", font=("Helvetica", 80, 'bold'), fill="Black")

        # Intro Graph Button
        self.graphBtn = tk.PhotoImage(file='factory/image/graphButton.png')
        graphButton = tk.Button(self, image=self.graphBtn,  borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame("GraphPage"))
        self.canvas.create_window(400, 700, window=graphButton)
        # self.canvas.create_window(0, 0, window=graphButton, anchor="nw")

        # Intro Start Button
        self.startBtn = tk.PhotoImage(file='factory/image/startButton.png')
        startButton = tk.Button(self, image=self.startBtn, borderwidth=0, highlightthickness=0,
                            command=lambda: controller.show_frame("StartPage"))
        self.canvas.create_window(1030, 700, window=startButton)




    # GIF animation
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return
        self.after(1, lambda: self.animate((counter+1) % len(self.sequence)))
