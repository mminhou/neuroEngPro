from module import *
from completePage import *

class Level1Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.backBtn = tk.PhotoImage(file='factory/image/backButton.png')
        self.goImage = tk.PhotoImage(file='factory/image/go1.png')
        self.nogoImage = tk.PhotoImage(file='factory/image/nogo1.png')
        self.exitImage = tk.PhotoImage(file='factory/image/exit1.png')
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
            [2, 1, 0, 0],
        ]

        # src position -> real screen position
        self.srcX = self.srcY = 0
        # Destination (x, y) based on gameMap
        self.dstX = self.dstY = 0
        # Position (x, y) based on gameMap
        self.posX = self.posY = 0

        for r in range(4):
            for c in range(4):
                # Path
                if self.gameMap[r][c] == 1:
                    self.canvas.create_image(c * 170 + 470, r * 170 + 200, image=self.goImage)
                # Non Path
                elif self.gameMap[r][c] == 0:
                    self.canvas.create_image(c * 170 + 470, r * 170 + 200, image=self.nogoImage)
                # Destination
                elif self.gameMap[r][c] == 3:
                    self.canvas.create_image(c * 170 + 470, r * 170 + 200, image=self.exitImage)
                    self.dstX = c
                    self.dstY = r
                # Player
                elif self.gameMap[r][c] == 2:
                    self.srcX = c * 170 + 470
                    self.srcY = r * 170 + 200
                    self.posX = c
                    self.posY = r

        self.player = Player(self.canvas, self.srcX, self.srcY)
        self.canvas.bind('<Left>', lambda _: self.leftSide())
        self.canvas.bind('<Right>',
                         lambda _: self.rightSide())
        self.canvas.bind('<Up>',
                         lambda _: self.upSide())
        self.canvas.bind('<Down>',
                         lambda _: self.downSide())

        # Previous Button
        self.backBtn = tk.PhotoImage(file='factory/image/exitButton2.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                               borderwidth=0, highlightthickness=0,
                                  command=lambda: controller.show_frame("StartPage"))
        self.canvas.create_window(1375, 60, window=backButton)

        # 제한 시간 관련
        self.remaining = 0
        self.countdown(10)

    def isCollide(self):
        if self.posX < 0:
            return True
        if self.posX >= 4:
            return True
        if self.posY < 0:
            return True
        if self.posY >= 4:
            return True
        if self.gameMap[self.posY][self.posX] == 0:
            return True
        return False

    def leftSide(self):
        self.posX -= 1
        if self.isCollide():
            self.posX += 1
        else:
            self.player.move(-170, 0)
            if self.isDst(self.posX, self.posY):
                print("Destination!")
                # time.sleep(0.2)
                self.controller.show_frame("CompletePage", 180-self.remaining)

    def rightSide(self):
        self.posX += 1
        if self.isCollide():
            self.posX -= 1
        else:
            self.player.move(170, 0)
            if self.isDst(self.posX, self.posY):
                print("Destination!")
                # time.sleep(0.2)
                self.controller.show_frame("CompletePage", 180-self.remaining)

    def upSide(self):
        self.posY -= 1
        if self.isCollide():
            self.posY += 1
        else:
            self.player.move(0, -170)
            if self.isDst(self.posX, self.posY):
                print("Destination!")
                # time.sleep(0.2)

                self.controller.show_frame("CompletePage", 180-self.remaining)

    def downSide(self):
        self.posY += 1
        if self.isCollide():
            self.posY -= 1
        else:
            self.player.move(0, 170)
            if self.isDst(self.posX, self.posY):
                print("Destination!")
                # time.sleep(0.2)
                self.controller.show_frame("CompletePage", 180-self.remaining)

    def isDst(self, x, y):
        if x == self.dstX and y == self.dstY:
            # print(180-self.remaining)
            # CompletePage.time = 180-self.remaining
            # self.controller.show_frame["CompletePage"].time = 180-self.remaining
            return True

    # 제한시간 정의
    def countdown(self, remaining=None):
        self.canvas.delete('ctime')
        if remaining is not None:
            self.remaining = remaining

        if int(self.remaining) <= 0:
            self.controller.show_frame('FailPage')
            # self.canvas.create_text(text="time's up!")
        else:
            self.canvas.create_text(1020, 60, text="%d:%d" % (int(self.remaining / 60), int(self.remaining % 60)),
                                    font=("Helvetica", 70, 'bold'), tags=('ctime'))
            self.remaining = self.remaining - 1
            # self.canvas.delete('ctime')
            # 플레이 시간 초 추가
            self.after(1000, self.countdown)


class MoveObject:
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

class Player(MoveObject):
    def __init__(self, canvas, x, y):
        self.pImage = tk.PhotoImage(file='factory/image/player1.png')
        self.player = canvas.create_image(x, y, image=self.pImage)
        super(Player, self).__init__(canvas, self.player)

