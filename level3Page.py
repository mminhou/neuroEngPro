from module import *
from processing import *

class Global():
    ''' Global Time class for timer '''
    count_time = 0

class Level3Page(tk.Frame):
    ''' Level3Page '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ''' Define initial images '''
        self.backBtn = tk.PhotoImage(file='factory/image/backButton.png')
        self.goImage = tk.PhotoImage(file='factory/image/go3.png')
        self.nogoImage = tk.PhotoImage(file='factory/image/nogo3.png')
        self.exitImage = tk.PhotoImage(file='factory/image/exit3.png')

        '''  Level3 Wallpaper '''
        self.canvas = tk.Canvas(self, width=1600, height=1200)
        self.canvas.pack()

        ''' Level3 Title '''
        self.canvas.create_text(720, 60, text="Level3", font=("Helvetica", 70, 'bold'))

        ''' Level3 Map '''
        self.gameMap = [
            [0, 1, 1, 1, 3],
            [0, 1, 0, 1, 1],
            [0, 1, 0, 1, 0],
            [1, 1, 1, 1, 0],
            [2, 1, 0, 0, 0]
        ]

        ''' Initial position '''
        self.srcX = self.srcY = 0
        self.dstX = self.dstY = 0
        self.complete = False
        self.posX = self.posY = 0

        for r in range(5):
            for c in range(5):
                if self.gameMap[r][c] == 1:
                    ''' Path '''
                    self.canvas.create_image(c * 142 + 410, r * 142 + 170, image=self.goImage)
                elif self.gameMap[r][c] == 0:
                    ''' Non Path '''
                    self.canvas.create_image(c * 142 + 410, r * 142 + 170, image=self.nogoImage)
                elif self.gameMap[r][c] == 3:
                    ''' Destination '''
                    self.canvas.create_image(c * 142 + 410, r * 142 + 170, image=self.exitImage)
                    self.dstX = c
                    self.dstY = r
                elif self.gameMap[r][c] == 2:
                    ''' Player '''
                    self.srcX = c * 142 + 410
                    self.srcY = r * 142 + 170
                    self.posX = c
                    self.posY = r

        ''' Create player -> Draw Real canvas position '''
        self.player = Player(self.canvas, self.srcX, self.srcY)
        ''' 
            KeyBoard binding
            <Left> Pressed -> call leftSide()
            <Right> Pressed -> call rightSide()
            <Up> Pressed -> call upSide()
            <Down> Pressed -> call downSide() 
        '''
        self.canvas.bind('<Left>', lambda _: self.leftSide())
        self.canvas.bind('<Right>', lambda _: self.rightSide())
        self.canvas.bind('<Up>', lambda _: self.upSide())
        self.canvas.bind('<Down>', lambda _: self.downSide())

        ''' Previous Button '''
        self.backBtn = tk.PhotoImage(file='factory/image/exitButton2.png')
        # self.graphBtn = self.graphBtn.subsample(4, 4) # Resizing button
        backButton = tk.Button(self, image=self.backBtn,
                                borderwidth=0, highlightthickness=0,
                                command=lambda: controller.show_frame("StartPage"))
        self.canvas.create_window(1375, 60, window=backButton)

        ''' Path Button '''
        setPathButton = tk.Button(self, text="PATH", font=("Helvetica", 50, 'bold'), borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: self.rawdataPath())
        self.canvas.create_window(60, 100, window=setPathButton, anchor="nw")

    def isCollide(self):
        ''' If there are block (gameMap range condition check) -> True, else False '''
        if self.posX < 0:
            return True
        if self.posX >= 5:
            return True
        if self.posY < 0:
            return True
        if self.posY >= 5:
            return True
        if self.gameMap[self.posY][self.posX] == 0:
            return True
        return False

    def leftSide(self):
        ''' Go left -> gameMap posX - 1 '''
        self.posX -= 1
        if self.isCollide():
            ''' If isCollide -> true, Restoration posX '''
            self.posX += 1
        else:
            ''' 
                Play moving from current to (currentX-115, currentY)
                Check arrived in destination
            '''
            self.player.move(-142, 0)
            self.isDst(self.posX, self.posY)

    def rightSide(self):
        ''' Go right -> gameMap posX + 1 '''
        self.posX += 1
        if self.isCollide():
            ''' If isCollide -> true, Restoration posX '''
            self.posX -= 1
        else:
            ''' Play moving from current to (currentX+115, currentY)'''
            self.player.move(142, 0)
            self.isDst(self.posX, self.posY)

    def upSide(self):
        ''' Go up -> gameMap posY - 1 '''
        self.posY -= 1
        if self.isCollide():
            ''' If isCollide -> true, Restoration posY '''
            self.posY += 1
        else:
            ''' Play moving from current to (currentX, currentY-115)'''
            self.player.move(0, -142)
            self.isDst(self.posX, self.posY)

    def downSide(self):
        ''' Go up -> gameMap posY + 1 '''
        self.posY += 1
        if self.isCollide():
            ''' If isCollide -> true, Restoration posY '''
            self.posY -= 1
        else:
            ''' Play moving from current to (currentX, currentY+115)'''
            self.player.move(0, 142)
            self.isDst(self.posX, self.posY)

    def isDst(self, x, y):
        ''' Checking (x, y) in gameMap is destination '''
        if x == self.dstX and y == self.dstY:
            ''' Detination??? ??????????????? True '''
            print("Destination!")
            self.complete = True
            ''' Call fp2GraphImage function for drawing graph '''
            fp2GraphImage(self.rawdataFilename[:-11] + 'Biomarkers.txt', 3000 - self.remaining)
            ''' Switch frame -> completePage '''
            self.controller.show_frame("CompletePage")
            return True

    def countdown(self, remaining=None):
        ''' Define Timer countdown '''
        self.canvas.delete('ctime') ### delete ctime in canvas
        if remaining is not None:
            ''' remaining update '''
            self.remaining = remaining

        if int(self.remaining) <= 0 and self.complete == False:
            ''' If time's up -> go to failpage '''
            self.controller.show_frame("FailPage")
        else:
            ''' ????????? margin 10s??? p300 ????????? ??? cycle(6s)??? ?????? ??? ?????? processing start '''
            if int(self.remaining) == 2984:
                self.processing()

            # self.canvas.create_text(1020, 60, text="%d:%d" % (int(self.remaining / 60), int(self.remaining % 60)),
            #                             font=("Helvetica", 70, 'bold'), tags=('ctime'))
            self.remaining = self.remaining - 1
            f = open('factory/image/play_time.txt', 'w+t')
            Global.count_time += 1
            playTxt = str(self.remaining)
            f.write(playTxt)
            f.close()
            self.after(1000, self.countdown)

    def rawdataPath(self):
        ''' Rawdata.txt's path setting '''
        self.rawdataFilename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("text files", "*.txt"),
                                                         ("all files", "*.*")))
        ''' start timer(3000s) after path setting '''
        self.countdown(3000)

    def processing(self):
        ''' Checking on complete '''
        if self.complete:
            return
        ''' Processing start by Rawdata.txt '''
        result = p300Processing2(self.rawdataFilename)
        ''' Moving by result condition '''
        if  result == 'up':
            self.upSide()
        elif result == 'down':
            self.downSide()
        elif result == 'left':
            self.leftSide()
        elif result == 'right':
            self.rightSide()
        else:   # ????????????
            return
        self.after(6000, self.processing)  # repeat processing function every 6000ms

class MoveObject:
    ''' Object class for player's moving '''
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

class Player(MoveObject):
    ''' Player class '''
    def __init__(self, canvas, x, y):
        self.pImage = tk.PhotoImage(file='factory/image/player3.png')
        self.player = canvas.create_image(x, y, image=self.pImage)
        super(Player, self).__init__(canvas, self.player)
