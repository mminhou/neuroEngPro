from module import *

class CompletePage(tk.Frame):
    ''' CompletePage '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.time = 0

        ''' Complete Wallpaper '''
        self.canvas = tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack(fill="both", expand=True)

        ''' Complete Title '''
        self.canvas.create_text(700, 200, text="Clear!", font=("Helvetica", 80, 'bold'), fill="Red")

        ''' Show paly Time txt  '''
        self.canvas.create_text(700, 300, text="Play Time >> press 'a' key", font=("Helvetica", 70, 'bold'), fill='Green')
        self.canvas.bind('<a>', lambda _: self.read_txt())

        '''  Go Home(Intro Button) Button '''
        homeButton = tk.Button(self, text="go home",
                               font=("Helvetica", 80, 'bold'),
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(700, 500, window=homeButton)

    def read_txt(self):
        ''' read play_time.txt '''
        self.f = open('factory/image/play_time.txt', 'r+t')
        self.a = self.f.readline()
        self.b = (int)(self.a)
        self.print_time = 180 - self.b
        self.k = "플레이 시간 : " + str(self.print_time)
        self.canvas.create_text(730, 400, text=self.k, font=('Helvetica', 30, "bold"))