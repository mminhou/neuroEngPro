from module import *

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.graphWall = tk.PhotoImage(file='factory/graphSampleImage2.png')
        # Wallpaper
        self.canvas = tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack(fill="both", expand=True)

        # Graph Title
        self.canvas.create_text(350, 100, text="Total Record", font=("Helvetica", 70, 'bold'))

        # Graph Image
        self.image = self.canvas.create_image(740, 500, image=self.graphWall)

        # Previous Button
        self.backBtn = tk.PhotoImage(file='factory/exitButton.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(1375, 60, window=backButton)



        # label = tk.Label(self, text="This is Graph Page", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("IntroPage"))
        # button.pack()