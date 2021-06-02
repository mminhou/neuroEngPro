from module import *
import math

class CompletePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.time = 0

        # Wallpaper
        self.canvas = tk.Canvas(self, width=800, height=600, bg='white')
        self.canvas.pack(fill="both", expand=True)

        # Title
        self.canvas.create_text(700, 200, text="Clear!", font=("Helvetica", 80, 'bold'), fill="Red")

        # 플레이 시간 계산
        if self.time / 60 >= 1:
            self.play_time = "플레이 시간 : " + str(math.trunc(self.time / 60)) + "분" + str(self.time % 60) + "초"
        else:
            self.play_time = "플레이 시간 : " + str(self.time) + "초"

        # 플레이 시간 출력
        self.canvas.create_text(700, 400, text=self.play_time, font=('Helvetica', 70, "bold"))

        # Graph Image
        # self.image = self.canvas.create_image(740, 500, image=self.graphWall)

        # Graph Image
        # self.image = self.canvas.create_image(740, 500, image=self.graphWall)

        # Previous Button
        self.backBtn = tk.PhotoImage(file='factory/image/exitButton.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                               command=lambda: controller.show_frame("IntroPage"))
        self.canvas.create_window(1375, 60, window=backButton)

