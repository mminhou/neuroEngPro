from module import *
from introPage import *
from graphPage import *
from startPage import *
from level1Page import *
from level2Page import *
from level3Page import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Neuro")
        # self.w = 1600
        # self.h = 1200
        # self.sw = self.winfo_screenwidth()
        # self.sh = self.winfo_screenheight()
        # self.x = (self.sw-self.w)/2
        # self.y = (self.sh-self.h)/2

        self.geometry("1600x1200")
        # self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # main container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (IntroPage, GraphPage, StartPage, Level1Page, Level2Page, Level3Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("IntroPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        frame.canvas.focus_set()
        # print(frame.canvas.focus_get())



if __name__ == "__main__":
    app = App()
    app.mainloop()