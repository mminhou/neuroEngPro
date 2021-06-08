from module import *

class IntroPage(tk.Frame):
    ''' IntroPage '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ''' Intro Wallpaper '''
        self.canvas = tk.Canvas(self, width=1200, height=1000)
        self.canvas.pack(fill="both", expand=True)
        ''' sequence For gif process -> animating gif images '''
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(
            Image.open(r'factory/image/original2.gif')
        )]
        self.image = self.canvas.create_image(720, 400, image=self.sequence[0])
        self.animating = True
        self.animate(0)

        ''' Graph Button '''
        self.graphBtn = tk.PhotoImage(file='factory/image/graphButton.png')
        graphButton = tk.Button(self, image=self.graphBtn, borderwidth=0, highlightthickness=0,
                                command=lambda: controller.show_frame("GraphPage"))
        self.canvas.create_window(400, 700, window=graphButton)

        ''' Intro Start Button '''
        self.startBtn = tk.PhotoImage(file='factory/image/startButton.png')
        startButton = tk.Button(self, image=self.startBtn, borderwidth=0, highlightthickness=0,
                                command=lambda: controller.show_frame("StartPage"))
        self.canvas.create_window(1030, 700, window=startButton)


    def animate(self, counter):
        ''' GIF animation '''
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return
        self.after(1, lambda: self.animate((counter+1) % len(self.sequence)))