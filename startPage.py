from module import *
from tkinter import filedialog
from processing import *

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.wall = tk.PhotoImage(file='factory/image/startWall.png')
        self.level2Btn = tk.PhotoImage(file='factory/image/level2.png')
        self.level3Btn = tk.PhotoImage(file='factory/image/level3.png')
        self.level1Btn = tk.PhotoImage(file='factory/image/level1.png')
        self.backBtn = tk.PhotoImage(file='factory/image/exitButton.png')

        # Start Canvas
        self.canvas = tk.Canvas(self, width=1600, height=1200)
        self.canvas.pack(fill="both", expand=True)
        self.image = self.canvas.create_image(740, 500, image=self.wall)

        # Fp2 filePath Button -> 일단 rawData
        fp2Button = tk.Button(self, text="FP2", font=("Helvetica", 80, 'bold'), borderwidth=0, highlightthickness=0,
                              command=lambda: self.rawdataPath())
        self.canvas.create_window(450, 100, window=fp2Button, anchor="nw")

        # Biomarkers filePath Button
        # biomarkersButton = tk.Button(self, text="BIO", font=("Helvetica", 80, 'bold'), borderwidth=0, highlightthickness=0,
        #                       command=lambda: self.path())
        # self.canvas.create_window(850, 100, window=biomarkersButton, anchor="nw")

        # Level2 Button
        level1Button = tk.Button(self, image=self.level1Btn, borderwidth=0, highlightthickness=0,
                                command=lambda: [self.rawdataPath(), controller.show_frame("Level1Page")])
        self.canvas.create_window(310, 490, window=level1Button)

        # Level3 Button
        level2Button = tk.Button(self, image=self.level2Btn, borderwidth=0, highlightthickness=0,
                                   command=lambda: controller.show_frame("Level2Page"))
        self.canvas.create_window(710, 490, window=level2Button)

        # Level1 Button
        level3Button = tk.Button(self, image=self.level3Btn, borderwidth=0, highlightthickness=0,
                                   command=lambda: controller.show_frame("Level3Page"))
        self.canvas.create_window(1110, 490, window=level3Button)

        # Exit Button
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(1375, 60, window=backButton)

    def rawdataPath(self):
        self.rawdataFilename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                                         ("all files", "*.*")))
        print(self.rawdataFilename)
        p300Processing(self.rawdataFilename)
