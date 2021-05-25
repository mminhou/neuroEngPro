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
        self.title("WTF")
        self.geometry("1600x1200")
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



if __name__ == "__main__":
    app = App()
    app.mainloop()